import joblib

print("=== POS SORTIR OTOMATIS PABRIK KOPI V2 === \n")

try:
    otak_ai = joblib.load("otak_kopi_pipeline.joblib")
    print(" [SISTEM] Otak AI Berhasil Dihidupkan Kembali !\n")

except:
    print(" [EOROR] File 'otak_kopi_pipeline.joblib' tidak ditemukan , pastikan nama filenya benar")

print("Silahkan Masukkan Dara Sensor Biji Kopi Baru: ")
input_ukuran = float(input(" - Masukkan Ukuran Biji (mm) : " ))
input_gelap = float(input(" - Masukkan Tingkat Kegelapan (1 - 10) :"))

print("\n [SATPAM] Sedang memeriksa daata")

if input_ukuran <= 0 or input_gelap <=0 :
    print("[SATPAM] AKTOR REJECT Anga tidak boleh minus atau no ! " )
elif input_gelap >10:
    print(" [SATPAM] AKTOR REJECT! Tingkat kegelapan maksimal adalah 10 !")
else:
    print(" [SATPAM] Data Aman! Silahkan masuk ke mesin penyortiran")

    data_baru = [[input_ukuran, input_gelap]]

    kode_tebakan = otak_ai.predict(data_baru)[0]

    if kode_tebakan == 0 :
        kategori = "PREMIUM (0)"
    
    elif kode_tebakan == 1 :
        kategori = "STANDAR (1)"

    else: 
        kategori = "CACAT/REJECT (2)"

    print(f"\n [HASIL NYATA] AI Menetapkan Kopi ini Masuk Kategori : {kategori}")