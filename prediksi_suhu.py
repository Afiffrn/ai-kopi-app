import numpy as np
from sklearn.linear_model import LinearRegression

print("== Melatih Model AI Pertama Anda (Regeresi Linier) ===]n")

waktu_mesin = np.array([[1], [2], [3], [4], [5]])

suhu_mesin = np.array([20, 25, 30, 35, 40])

otak_ai = LinearRegression()

otak_ai.fit(waktu_mesin, suhu_mesin)

print ( " Latihan Selesai ! , Model AI Anda sudah pintar")


menit_baru = np.array([[350]])
tebakan_ai = otak_ai.predict(menit_baru)

print(f" Hasil Tebakan AI untuk Menit ke- 6 adalaah: {tebakan_ai[0]} C]")

