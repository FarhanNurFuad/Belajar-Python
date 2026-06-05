#Membuat Dictionary
mahasiswa = {
    "nama" : "Farhan",
    "umur" : 25,
    "kota" : "Bandung"
}

#Mengambil Dictionary
print(mahasiswa["nama"])
print(mahasiswa["umur"])
print(mahasiswa["kota"])
print()

#Menampilkan Semua Data
print(mahasiswa)

#Mengubah Data
mahasiswa["umur"] = 24

print (mahasiswa)
print()

#Menambah Data Baru
mahasiswa["jurusan"] = "Sistem Informasi"
print(mahasiswa)
print()

#Menghapus Data
del mahasiswa["kota"]
print(mahasiswa)
print()

#Loop Dictioanry
#Menampilkan Key
for key in mahasiswa:
    print(key)
print()

#Menampilkan Value
for key in mahasiswa:
    print(mahasiswa[key])
print()

#Meanmpilakn Key dan Value
for key, value in mahasiswa.items():
    print(key, ":", value)
print()

#Input ke Dictionary
nama = input("Masukkan Nama :")
umur = int(input("Masukkan Umur :"))

mahasiswa={
    "nama" : nama,
    "umur" : umur
}

print(mahasiswa)
print()

#List Berisi Dictioanary
mahasiswa = {
    "nama" : "Farhan",
    "umur" : "25"
},
{
    "nama" : "Andi",
    "umur" : "20"
}

print(mahasiswa[0]["nama"])