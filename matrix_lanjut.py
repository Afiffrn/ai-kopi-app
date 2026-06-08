import numpy as np

data_pabrik = [
    [26.5, 75.0, 1011.2],
    [27.0, 74.2, 1011.5],
    [26.8, 73.8, 1010.8],  # Detik ke-3 (Indeks baris 2)
    [27.2, 75.5, 1012.0],  # Detik ke-4 (Indeks baris 3)
    [26.9, 76.0, 1011.1]

]

matrix_sensor = np.array(data_pabrik)


potongan_khusus = matrix_sensor [2:, 1:]

print("== Hasil Potongan Matriks Khusus ==")
print(potongan_khusus)