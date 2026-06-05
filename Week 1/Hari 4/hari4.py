#Contoh LOOP

for i in range(5):
    print("Belajar Pyython")
print()

#Pengunaan for loop
for i in range (5):
    print(i)
print ()

#Pengunaan Range
#Contoh Range Awal-Akhir
for i in range (1, 6):
    print(i)
print()

#Contoh Range dengan Kelipatan
for i in range (0, 11, 2):
    print (i)
print()

#Menggunakan variable pada loop
nama = "farhan"

for i in range(3):
    print(nama)
print()

#Pengunaan While Loop
angka = 1

while angka <= 5:
    print (angka)
    angka += 1
print()

#Infinite Loop
angka = 1

while angka <= 5:
    print (angka)
#Kalau Tanpa syntax dibawah loop tidak akan berhenti
    angka += 1
print()

#Menghitung Total
total = 0

for i in range(1 ,6) :
    total += i

print (total)
print()

#Tabel Perkalian
angka = int(input("masukan Angka :"))

for i in range (1, 11):
    print (f"{angka} x {i} = {angka * i}")
print()

#Loop dengan input pengguna
jumlah = int(input("Berapa Kali ingin ditampilkan :"))

for i in range(jumlah) :
    print ("Belajar Python")