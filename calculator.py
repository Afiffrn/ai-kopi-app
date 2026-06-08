print("=== KALKULATOR SEDERHANA SAYA ===")
print("Pilih Operasi:")
print("1. Penjumlahan ")
print("2. pengurangan")
print("3. Perkalian")
print("4.Pembagian")

pilihan = input("Masukkan pilihan operasi: ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))


if pilihan == '1':
	hasil = angka1 + angka2
	print(f"Hasil : {hasil}")

elif pilihan == '2':
	hasil = angka1 - angka2
	print(f"Hasil : {hasil}")

elif pilihan == '3':
	hasil = angka1 * angka2
	print(f"Hasil : {hasil}")

elif pilihan == '4':
	hasil = angka1 / angka2
	print(f"Hasil : {hasil}")

else :
	print("Pilihan operasi tidak valid !!")


