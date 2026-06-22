#Memecah String
nama = "Farhan"

print(nama[0:3])
print()

#Slice dari awal sampai Akhir
#Dari awal sampai index tertentu
teks = "BelajarPython"

print(teks[:7])
print()

#Dari index tertentu sampai akhir
teks = "BelajarPython"

print(teks[7:])
print()

#Slice dengan Langkah
kata = "ABCDEFGHIJ"

print(kata[::3])
print()

#Membalik String
kata = "Farhan"

print(kata[::-1])
print()

#Membersihkan input User
nama = input("Masukkan nama: ").strip().title()

print(nama)
print()

#F-String Lebih Rapi
nama = "Farhan"
umur = 20
kota = "Bekasi"

print(f"Nama saya {nama}, umur saya {umur} tahun, saya tinggal di {kota}.")
print()

#Format Angka Decimal
bmi = 24.857192

print(f"BMI saya adalah {bmi:.2f}")
print()

#Menggabungkan Banyak Data dengan F-String
nama = "Farhan"
nilai = 88.456

print(f"Nama: {nama}")
print(f"Nilai akhir: {nilai:.2f}")
print()

#Split Data dari input
data = input("Masukkan data (nama-umur-kota): ")

hasil = data.split("-")

print(hasil)

#Ambil Satu-Satu
data = input("Masukkan data (nama-umur-kota): ")
hasil = data.split("-")

nama = hasil[0]
umur = hasil[1]
kota = hasil[2]

print("Nama :", nama)
print("Umur :", umur)
print("Kota :", kota)
print()

#Join Menggabungka Kata
kata = ["Saya", "sedang", "belajar", "Python"]
hasil = " ".join(kata)

print(hasil)
print()

#Validasi Email Sederhana
email = input("Masukkan email: ").strip()

if "@" in email and "." in email:
    print("Email valid")
else:
    print("Email tidak valid")
print()

#Membuat Output Tabel Sederhana
nama = "Farhan"
umur = 20
kota = "Bekasi"

print("===== BIODATA =====")
print(f"Nama : {nama}")
print(f"Umur : {umur}")
print(f"Kota : {kota}")