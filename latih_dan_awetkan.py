import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

print("== LANGKAH 1 : Melatih dan Mengawetkan Otak AI ===\n")

fitur_kopi = np.array([[9.5, 8], [8.0, 6], [9.0, 9], [8.2, 7], [4.0, 2], [5.0, 3]])
label_kualitas = np.array([0, 1, 0, 1, 2, 2])

ahli_sortir = DecisionTreeClassifier(random_state=42)
ahli_sortir.fit(fitur_kopi, label_kualitas)
print(" [STATUS] AI Selesai Latihan.")

joblib.dump(ahli_sortir, "otak_kopi.joblib")

print(" [STATUS] Sukses! Otak AI telah diawerkan menjadi file 'otak_kopi.joblib' !  ")