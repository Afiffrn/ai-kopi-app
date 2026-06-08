import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.tree import DecisionTreeClassifier

print("=== INTI UTAMA: SYSTEM INTEGRATION AI SMART FACTORY ===\n")

# =====================================================================
# PART 1 & 2: TRAINING PHASE (Masa Lalu - Membangun Otak AI)
# =====================================================================

# A. Data Sejarah untuk Satpam AI (Deteksi Anomali) -> [Ukuran, Warna]
data_keamanan_normal = np.array([
    [9.0, 8], [8.5, 7], [9.2, 8], [8.0, 6], [8.8, 7],
    [9.1, 8], [8.6, 7], [9.4, 9], [8.2, 6], [8.9, 8]  # <-- Tambahan data normal baru
])
# Kembalikan ke 0.1 karena datanya sudah banyak dan kuat
satpam_ai = IsolationForest(contamination=0.1, random_state=42)
satpam_ai.fit(data_keamanan_normal)

# B. Data Sejarah untuk Ahli Sortir (Klasifikasi) -> 0=Premium, 1=Standar
fitur_kopi = np.array([
    [9.5, 8], [8.0, 6], [9.0, 9], [8.2, 7]
])
label_kualitas = np.array([0, 1, 0, 1])

ahli_sortir = DecisionTreeClassifier(random_state=42)
ahli_sortir.fit(fitur_kopi, label_kualitas)

print("⚙️ [STATUS] Semua Otak AI Berhasil Dilatih & Diintegrasikan!\n")

# =====================================================================
# PART 4 & 5: PRODUCTION PHASE (Masa Depan - Sistem Berjalan Otomatis)
# =====================================================================

# Bayangkan ini data mentah yang baru dikirim oleh sensor IoT ban berjalan
# Data 1: Normal Premium, Data 2: Kabel putus/Eror, Data 3: Serangan Siber (Suhu/Ukuran minus)
data_sensor_iot = np.array([
    [9.1, 8.0],
    [999.0, 7.0],  # Eror fisik sensor
    [1.0, 9.0]     # Anomali ekstrem / Sabotase
])

print("🤖 Menjalankan Pemindaian Otomatis Terintegrasi...\n")

# Loop menyisir setiap data yang masuk dari ban berjalan
for i, data in enumerate(data_sensor_iot):
    print(f"--- Memeriksa Objek ke-{i+1}: {data} ---")
    
    # KONDISI 1: Pembersihan Awal (Ilmu NumPy Fase 2)
    if data[0] == 999.0 or data[1] == 999.0:
        print("❌ STATUS: GAGAL! Sensor Rusak (Terdeteksi Angka 999.0). Data Dibuang!")
        continue
        
    # Memformat data menjadi Matriks 2D agar bisa dibaca AI
    data_siap_uji = np.array([data])
    
    # KONDISI 2: Uji Keamanan Siber (Satpam AI - Anomali)
    status_keamanan = satpam_ai.predict(data_siap_uji)[0]
    if status_keamanan == -1:
        print("🚨 STATUS: BAHAYA! Terdeteksi Anomali Ekstrem/Serangan Siber! Blokir Data!")
        continue
        
    # KONDISI 3: Jika Lolos Semua, Masuk ke Ahli Sortir AI (Klasifikasi)
    kategori = ahli_sortir.predict(data_siap_uji)[0]
    if kategori == 0:
        print("🌟 STATUS: SUKSES! Biji Kopi KUALITAS PREMIUM (Masuk Kantong A)")
    else:
        print("📦 STATUS: SUKSES! Biji Kopi KUALITAS STANDAR (Masuk Kantong B)")