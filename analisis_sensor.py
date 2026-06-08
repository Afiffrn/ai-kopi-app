import numpy as np

print("--- Eksplorasi Data Sensor dengan NumPy --- \n")

# 1. Simulasikan data mentah dari sensor IoT (ada 2 data yang eror/rusak: -99.0 dan 85.0)
data_mentah = [-50, 26.5, 27.0, -99.0, 26.8, 27.2, 85.0, 26.9, 27.1, 26.6, 26.8]

# 2. Mengubah list Python biasa menjadi Array NumPy (ndarray)
# Ini membuat proses matematika menjadi jauh lebih cepat
array_suhu = np.array(data_mentah)

print(f"Data Mentah Asli: \n{array_suhu}\n")

# 3. Teknik Masking (Penyaringan Otomatis)
# Kita hanya ingin mengambil data suhu ruangan yang masuk akal saja (antara 0 sampai 40 derajat)
data_valid = array_suhu[(array_suhu >= 0) & (array_suhu <= 40)]

print(f"Data Setelah Disaring (Eror Dibuang): \n{data_valid}\n")

# 4. Melakukan Analisis Statistik Cepat
suhu_rata_rata = np.mean(data_valid)
suhu_tertinggi  = np.max(data_valid)
suhu_terendah   = np.min(data_valid)

print("-" * 40)
print(f"📊 HASIL ANALISIS SENSOR:")
print(f"   - Rata-rata Suhu Asli : {round(suhu_rata_rata, 2)}°C")
print(f"   - Suhu Tertinggi      : {suhu_tertinggi}°C")
print(f"   - Suhu Terendah       : {suhu_terendah}°C")
print("-" * 40)