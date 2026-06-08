import pandas as pd

print("=== FASE 5 :Membaca Data Eksternal Menggunakan Pandas ===\n")

tabel_kopi = pd.read_csv("data_pabrik.csv")

print(" ISI TABEL DATA PABRIK :")
print(tabel_kopi)

print("\n INFO STRUKTUR TABEL :")

tabel_kopi.info()

print("\n--- EKSPERIMEN MEMOTONG DATA TABEL ---")

kolom_ukuran = tabel_kopi["ukuran_mm"]
print("\n Hanya Kolom Ukuran: ")

print(kolom_ukuran)

kopi_premium = tabel_kopi[tabel_kopi["kualitas"] == "Premium"]
print("\n Hanya Kopu Kualitas Premium: ")
print(kopi_premium)


print("\n=== ADVANCED MASKIN (DUA KONDISI)===")

kopi_super = tabel_kopi[(tabel_kopi["ukuran_mm"] > 8.5) & (tabel_kopi["tingkat_gelap"] > 7 )]

print("\n Kopi Spek uper (Ukuran > 8.5 & Gelap > 7): ")
print(kopi_super)