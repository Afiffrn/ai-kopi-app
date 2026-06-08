import numpy as np
import joblib

print(" === LANGKAH 2 : Menggunakan Otak AI Siap Pakai ===\n")

ai_impor = joblib.load("otak_kopi.joblib")
print(" [STATUS]File 'otak_kopi.joblib' berhasil dimuat ke dalam sistem ! ")

kopi_baru = np.array([[4.1, 2]])

tebakan = ai_impor.predict(kopi_baru)

print(f"\n Hasil Tebakan AI Instan: Biji kopi ini asuk ke KELAS {tebakan[0]}")


