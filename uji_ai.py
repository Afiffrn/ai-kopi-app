from sklearn.metrics import confusion_matrix, accuracy_score

print("== FASE 5: Menguji Perfotma AI (Evaluasi Model) ===\n")

kunci_jawaban = [0, 0, 0, 1, 1]

tebakan_ai = [0, 1, 0, 1, 1]

skor_akurasi = accuracy_score(kunci_jawaban, tebakan_ai)

tabel_bingung = confusion_matrix(kunci_jawaban, tebakan_ai)

print(f" TINGKAT AKURASI AI: {skor_akurasi * 100} %")

print("\n TAVEL CONFUSION MATRIX: ")

print(tabel_bingung)