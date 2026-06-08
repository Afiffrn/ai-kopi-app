import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

print("== FASE 6 : PIPELINE END-TO-END MACHINE LEARNING ===\n")

data_kopi = pd.read_csv("data_pabrik_v2.csv")
print(f" Total seluruh data di gudang: {len(data_kopi)} baris. \n")

X = data_kopi [["ukuran_mm", "tingkat_gelap"]]
y = data_kopi["kualitas"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print(" HASIL PEMBELAHAN DATA: ")
print(f" - Data Fitur Latihan (X_train) : {len(X_train)} baris")
print(f" - Data Ujian Akhir (X_test) : {len(X_test)} baris")
print(f" - Kunci Jawaban Ujian (y_test) : \n{y_test}")

print("\n--- LANGKAH 4 & 5 : RAIN & EVALUATE MODEL ---")

model_kopi = DecisionTreeClassifier(random_state=42)

model_kopi.fit(X_train, y_train)
print("[STATUS] AI Selesai mempelajari 8 baris data latihan.")

hasil_tebakan = model_kopi.predict(X_test)

skor_akurasi = accuracy_score(y_test, hasil_tebakan)
print(f"SKOR AKURASI AKHIR PIPELINE: {skor_akurasi * 100}%")

print("\n--- ANGKAH 6 : Model Deployment  (Pengawetan) ----")

joblib.dump(model_kopi, "otak_kopi_pipeine.joblib")
print(" [STATUS] Kemenangan Telak ! File 'otak_kopi_pipeline.joblib' Resmi diamankan ! " )


