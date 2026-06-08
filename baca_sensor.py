import paho.mqtt.client as mqtt

# Konfigurasi Alamat Server MQTT (Harus sama dengan si pengirim)
MQTT_BROKER = "localhost"
MQTT_TOPIC = "ruangan/suhu"

# Fungsi callback: Otomatis berjalan setiap kali ada data baru yang masuk
def ketika_ada_pesan(client, userdata, msg):
    # Mengubah data mentah (bytes) menjadi teks (string) lalu menjadi angka (float)
    data_suhu = float(msg.payload.decode())
    
    print(f"[BARU] Menerima data sensor: {data_suhu}°C")
    
    # Logika Sistem Tertanam: Berikan peringatan jika suhu overheat
    if data_suhu > 28.5:
        print("   ⚠️ PERINGATAN: Suhu ruangan terlalu panas! Nyalakan AC/Kipas!")
    else:
        print("   ✅ Kondisi ruangan aman.")
    print("-" * 40)

# Inisialisasi Client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Menghubungkan fungsi callback kita ke sistem MQTT
client.on_message = ketika_ada_pesan

print("Menghubungkan ke MQTT Broker...")
client.connect(MQTT_BROKER, 1883, 60)

# Berlangganan (Subscribe) ke topik yang ditentukan
client.subscribe(MQTT_TOPIC)
print(f"Sukses! Sekarang sedang menguping topik: {MQTT_TOPIC}")
print("Menunggu data masuk... (Tekan Ctrl + C untuk berhenti)\n")

# Menjalankan loop terus-menerus di latar belakang untuk menerima data
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nProgram penerima dihentikan. Sampai jumpa!")