import numpy as np
from sklearn.linear_model import LinearRegression

print("== Melatih Ai dengan banyajk faktor (multiple linear regression)")

faktor_mesin = np.array([
    [1, 50],   # Menit 1, Beban 50%
    [2, 60],   # Menit 2, Beban 60%
    [3, 70],   # Menit 3, Beban 70%
    [4, 80],   # Menit 4, Beban 80%
    [5, 90]

])

suhu_mesin = np.array([25, 32, 39, 46, 53])

otak_ai = LinearRegression()

otak_ai.fit(faktor_mesin, suhu_mesin)

print(" Latihan Selesai ! Otak AI Multi-Faktor Anda sudah siap. ")

# 4. Uji Coba AI: Prediksi untuk Menit ke-6 dengan Beban 100%
# Ingat: Input harus berupa Matriks 2D [[Menit, Beban]]
kondisi_baru = np.array([[2, 150]])
tebakan_ai = otak_ai.predict(kondisi_baru)

# Kita gunakan round(..., 2) agar hasilnya bulat dan cantik tanpa buntut pecahan biner
print(f"🔮 Hasil Tebakan AI Multi-Faktor untuk masa depan: {round(tebakan_ai[0], 2)}°C")