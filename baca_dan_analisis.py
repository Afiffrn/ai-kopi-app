import paho.mqtt.client as mqtt
import numpy as np

MQTT_BROKER = "localhost"
MQTT_TOPIC = "ruangan/suhu"

# Tempat menampung data sementara sebelum diolah NumPy
penampung_data = []
KAPASITAS_MAKSIMAL = 5

def ketika_ada_pesan(client, userdata, msg):
    global penampung_data
    
    # Ambil data mentah dan ubah menjadi angka float
    suhu = float(msg.payload.decode())
    print(f"[INPUT] Masuk data baru: {suhu}°C")
    
    # Masukkan ke dalam list penampung
    penampung_data.append(suhu)
    print(f"        Status penampung: {penampung_data} ({len(penampung_data)}/{KAPASITAS_MAKSIMAL})")
    
    # JIKA PENAMPUNG SUDAH PENUH (Mencapai 5 data), SAATNYA NUMPY BERAKSI!
    if len(penampung_data) == KAPASITAS_MAKSIMAL:
        print("\n" + "="*45)
        print("📊 PENAMPUNG PENUH! NumPy mulai menghitung...")
        
        # 1. Ubah list menjadi Array NumPy
        array_sensor = np.array(penampung_data)
        
        # 2. Filter data (Masking) - Anggap suhu di atas 40°C atau di bawah 10°C adalah data rusak
        data_valid = array_sensor[(array_sensor >= 10) & (array_sensor <= 40)]
        
        # 3. Hitung Statistik Cepat dengan NumPy
        rata_rata = np.mean(data_valid)
        suhu_maks  = np.max(data_valid)
        
        print(f"   -> Total data diproses : {len(array_sensor)}")
        print(f"   -> Rata-rata suhu saat ini: {round(rata_rata, 2)}°C")
        print(f"   -> Suhu tertinggi terdeteksi: {suhu_maks}°C")
        print("="*45 + "\n")
        
        # 4. Kosongkan kembali penampung untuk 5 data berikutnya
        penampung_data = []

# Inisialisasi Client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = ketika_ada_pesan

print("Menghubungkan ke MQTT Broker...")
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)

print("Sistem Real-Time Data Handling Aktif. Menunggu aliran data...\n")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSistem dihentikan.")