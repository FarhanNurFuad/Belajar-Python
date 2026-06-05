#List (Kumpulan data)
#Menampilkan List
buah = ["Apel", "Jeruk", "Mangga"]

print (buah)
print()

#Menagkses Data
buah = ["Apel", "Jeruk", "Mangga"]

print(buah[0])
print(buah[1])
print(buah[2])
print()

#Mengubah Data
buah = ["Apel", "Jeruk", "Mangga"]

buah[1] = "pisang"

print (buah)
print ()

#Menambah Data
buah = ["Apel", "Jeruk"]

buah.append("Mangga")

print(buah)
print()

#Menghapus Data
buah = ["Apel", "Jeruk", "Mangga"]

buah.remove("Jeruk")

print(buah)
print()

#Panjang List
buah = ["Apel", "Jeruk", "Mangga"]

print(len(buah))
print()

#Loop pada List
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    print(item)
print()

#Loop dengan Nomor Urut
buah = ["Apel", "Jeruk", "Mangga"]

for i in range(len(buah)):
    print(i, (buah[i]))
print()

#Input dalam List
daftar_nama = []

for i in range (3):
    nama = input("Masukkan Nama :")
    daftar_nama.append(nama)

print(daftar_nama)
