import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

print("== FASE 5 : Visuaisasi Confusion Matrix denga Heatmap ===\n")


kunci_jawaban = [0, 0, 0, 1, 1]
tebakan_ai = [ 0, 1, 0, 1, 1]

tabel_bingung = confusion_matrix(kunci_jawaban, tebakan_ai)

plt.figure(figsize = (6, 5))

sns.heatmap(
    tabel_bingung,
    annot=True, 
    fmt= "d", 
    cmap = "Blues", 
    xticklabels = ["Premium (0)", "Standar (1)"], 
    yticklabels = ["Premium (0)", "Standar(1)"]

)

plt.title("Visualisasi Rapor Performa AI (Confusion Matrix)", fontsize = 12, fontweight = 'bold')
plt.xlabel("Hasil Tebakan AI", fontsize = 10)
plt.ylabel("Kunci Jawaban Asli", fontsize = 10)

plt.savefig("grafik_rapor_ai.png")
print(" [STATUS] Sukses! Gambar grafik telah disimpan dengan nama 'grafik_rapor_ai.png'! ")