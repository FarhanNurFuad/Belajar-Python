daftar_nama = []

for i in range (5):
    nama = input("Masukan Nama :")
    daftar_nama.append(nama)

for i in range (len(daftar_nama)) :
    print (i+1, (daftar_nama[i]))