import paho.mqtt.client as mqtt
import time
import random

# 1. Konfigurasi Alamat Server MQTT
MQTT_BROKER = "localhost"
MQTT_TOPIC = "ruangan/suhu"

print("Memulai koneksi ke MQTT Broker...")

# 2. Inisialisasi Client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 3. Menghubungkan Python ke Server Mosquitto
client.connect(MQTT_BROKER, 1883, 60)

print(f"Berhasil terhubung! Mulai mengirim data ke topik: {MQTT_TOPIC}")
print("Tekan Ctrl + C di terminal untuk menghentikan program.\n")

# 4. Loop Otomatis untuk Mengirim Data Terus-menerus
try:
    while True:
        # Menyimulasikan angka suhu acak antara 25.0 sampai 30.0 derajat
        suhu_palsu = round(random.uniform(25.0, 30.0), 2)
        
        # Mengirimkan data suhu ke server MQTT
        # Data harus diubah menjadi string (teks) menggunakan str()
        client.publish(MQTT_TOPIC, str(suhu_palsu))
        
        print(f"[LOG] Data sensor terkirim ke Broker: {suhu_palsu}°C")
        
        # Jeda waktu 2 detik sebelum mengirim data berikutnya
        time.sleep(2)

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna. Sampai jumpa!")
    client.disconnect()