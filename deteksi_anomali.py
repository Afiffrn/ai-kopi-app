import numpy as np
from sklearn.ensemble import IsolationForest

print("=== Mengaktigkan AI Satpam (Deteksi Anomali IoT) ===\n")

data_normal = np.array([
    [26.5, 75.0],
    [27.0, 74.2],
    [26.8, 74.8],
    [27.2, 75.5],
    [26.9, 76.0]
])

satpam_ai = IsolationForest(contamination = 0.1, random_state = 42)
satpam_ai.fit(data_normal)

data_baru = np.array([
    [26.8, 74.5],
    [15.0, 95.0],
    [35.0, 50.0]
])

hasil_periksa = satpam_ai.predict(data_baru)

print( " Hasil Pemeriksaan AI (1 = Normal, -1 = Anomali/Bahaya)")
print(hasil_periksa)
