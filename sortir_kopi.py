import numpy as np
from sklearn.tree import DecisionTreeClassifier

print("== Mengaktifkan AI Ahli Sortir ( Klasifikasi Biki Kopi) ===\n")

fitur_kopi = np.array([
    [9.5, 8],  # Besar, Cokelat Pas
    [8.0, 6],  # Sedang, Agak Terang
    [4.0, 2],  # Kecil, Sangat Terang (Cacat)
    [9.0, 9],  # Besar, Cokelat Pas
    [5.0, 3]   # Kecil, Sangat Terang (Cacat)
])

label_kualitas = np.array([0, 1, 2, 0, 2])

ahli_sortir = DecisionTreeClassifier(random_state = 42)
ahli_sortir.fit(fitur_kopi, label_kualitas)

print (" Latihan Selsesai ! AI Ahli Sortir Anda suda hafas pola kualitas kopi. ")

kopi_misterius = np.array([
    [8.8, 7],
    [7.5, 5]
])
hasil_sortir = ahli_sortir.predict(kopi_misterius)

print(f" Hasil Klasigikasi AI : Bji kopi ini masuk ke KELAS {hasil_sortir}")