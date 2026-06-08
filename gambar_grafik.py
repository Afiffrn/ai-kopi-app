import pandas as pd
import matplotlib.pyplot as plt

print ("=== FASE 5 : Visualisasi Data Menggunakan Matplotlib ===\n")

data = pd.read_csv("data_pabrik.csv")

premium = data[data["kualitas"] == "Premium"]
standar = data[data["kualitas"] == "Standar"]
cacat = data[data["kualitas"] == "Cacat"]


plt.scatter(premium["ukuran_mm"], premium["tingkat_gelap"], color="green", label="Premium", s=100 )
plt.scatter(standar["ukuran_mm"], standar["tingkat_gelap"], color="blue" , label="Standar", s=100 )
plt.scatter(cacat["ukuran_mm"], cacat["tingkat_gelap"], color="red", label="Cacat", s=100)

plt.title("Grafik Analisis Kualitas Biki Kopi Pabrik", fontsize = 14)
plt.xlabel("Ukuran Biki Kopi (mm)", fontsize = 12)
plt.ylabel("Tingkat Kegelapan Warna" , fontsize = 12)
plt.legend()
plt.grid(True)

plt.savefig("grafik_kopi.png")
print(" [STATTUS] Sukses! Grafik telah disimpan dengan nama 'grafik_kopi.png' ! ")

