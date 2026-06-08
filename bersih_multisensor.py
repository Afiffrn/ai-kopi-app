import numpy as np

print("=== Sistem Pembersihan Data Multi-Sensor (Slicing + Masking) ===\n")

data_pabrik = [
    [26.5, 75.0, 1011.2],
    [27.0, 74.2, 1011.5],
    [26.8, 999.0, 1010.8],
    [85.0, 75.5, 1012.0],  # Detik ke-4: Sekarang Suhunya eror (85.0)
    [26.9, 76.0, 1011.1]
]

matrix_sensor = np.array(data_pabrik)

kolom_suhu = matrix_sensor [:, 0]
suhu_bersih = kolom_suhu [kolom_suhu <= 40]

rata_rata_suhu = np.mean(suhu_bersih)

print(f"Kondisi sebelum disaring : {kolom_suhu}")

print(f"Kondisi setelah disating : {suhu_bersih}")
print(f"Rata-rata suhu nya adalah : {rata_rata_suhu}")

kolom_kelembaban = matrix_sensor[:, 1]

kelembaban_bersih = kolom_kelembaban [kolom_kelembaban < 100 ]

print ( " Kondisi Kolom Kelembaban Sebelum Disaring : ")
print(kolom_kelembaban)

print("\n Hasil Setelah Disaring (Angka Eror Lenyap): ")
print(kelembaban_bersih)