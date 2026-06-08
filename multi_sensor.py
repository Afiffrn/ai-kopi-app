import numpy as np
print("=== Eksplorasi Multi-Sensor (Matriks 2D) dengan NumPy ===\n")

#1. simulasikan data yang masuk dari 3 sensor selama 5 detik berkala
# format per baris : [SUhu, Kelambaan , Tekanan]

data_pabrik = [
    [26.5, 75.0, 1011.2],  # Detik ke-1
    [27.0, 74.2, 1011.5],  # Detik ke-2
    [26.8, 999.0, 1010.8], # Detik ke-3 (Ada data kelembaban eror: 999.0)
    [27.2, 75.5, 1012.0],  # Detik ke-4
    [26.9, 76.0, 1011.1]   # Detik ke-5
]

matriks_sensor = np.array(data_pabrik)

print("Matriks Data @D Asli (Baris = Waktu, Kolom = Sensor) :")
print(matriks_sensor)
print(f"Bentuk Matriks (Shape) : {matriks_sensor.shape} - > (5 Baris, # Kolom)\n")
print("-" * 50)


kolom_suhu = matriks_sensor [: , 0 ]

kolom_kelembaban = matriks_sensor [:, 1]

print(f"Hasil Potongan Kolom Suhu Saja     : {kolom_suhu}")
print(f"Hasil Potongan Kolom Kelembaban Saja: {kolom_kelembaban}\n")
print("-" * 50)

# 4. Analisis Statistik pada Kolom Tertentu
# Mari hitung rata-rata suhu dari kolom indeks 0
rata_suhu = np.mean(kolom_suhu)
print(f"📊 Rata-rata Suhu Pabrik saat ini: {round(rata_suhu, 2)}°C")

print(f"Data kelembapan Asli: \n{kolom_kelembaban}\n")

# 3. Teknik Masking (Penyaringan Otomatis)
# Kita hanya ingin mengambil data suhu ruangan yang masuk akal saja (antara 0 sampai 40 derajat)
data_kelembaban_valid = kolom_kelembaban[kolom_kelembaban  < 100]

print(f"Data Setelah Disaring (Eror Dibuang): \n{data_kelembaban_valid}\n")

mean_kelembaban = np.mean(data_kelembaban_valid)

print(f"rata - rata kelembabannya adalah : {mean_kelembaban}")

# Eksperimen melihat isi "topeng" (mask) secara langsung
topeng_logika = kolom_suhu > 27
print("Isi dari topeng logika adalah:")
print(topeng_logika)