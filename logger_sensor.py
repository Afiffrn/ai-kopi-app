import csv 
import time
from datetime import datetime
import numpy as np

print("== Mengaktidkan Sistem Data Logging ke CSV +++\n")

NAMA_FILE = "log_data_pabrik.csv"

hasil_analisis_numpy = [
    [26.85, 75.18],
    [27.10, 74.90],
    [26.92, 75.55]
]

print(f"Mulai menulis data ke dalam file : {NAMA_FILE}...")

with open(NAMA_FILE, mode = 'a', newline = '') as file_csv :
    penulis_csv = csv.writer(file_csv)

    if file_csv.tell() == 0 :
        penulis_csv.writerow(["Waltu_Pencatatan", " Rata_Suhu", " Rata_Kelembaban" ])


    for data in hasil_analisis_numpy:
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        baris_baru = (waktu_sekarang, data[0], data[1])

        penulis_csv.writerow(baris_baru)
        print(f"[LOGGED] Berhasil mencatat : {baris_baru}" )

        time.sleep(1)

print(f"\n Selesai ! File '{NAMA_FILE}' BERHASIL")