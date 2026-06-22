#Mengakses Karakter
nama = "Farhan"

print(nama[4])
print()

#Index Negatif
nama = "Farhan"

print(nama[-1])
print()

#Panjang String
nama = "Farhan"

print(len(nama))
print()

#Huruf Besar dan Kecil
nama = "Farhan"
titl = "farhan nur Fuad"

print(nama.upper())
print(nama.lower())
print(titl.title())
print()

#Menghapus Spasi
nama = "            Farhan         "

print(nama.strip())
print()

#Mengganti Kata
kalimat = "Saya Suka anak Kecil"

print(kalimat.replace("anak", "barang"))
print()

#Mengecek Kata
kalimat = "Bleajar Python Gaes"

print("Python" in kalimat)
print()

#Menghitung Kemunculan Huruf
nama = "Farhan"

print(nama.count("a"))
print()

#Memecaah String
nama = "Farhan Nur Fuad"

data = nama.split()
print (data)
print()

#Menggabungkan String
kata = ["Saya", "Belajar", "Python"]

hasil = " ".join(kata)
print(hasil)