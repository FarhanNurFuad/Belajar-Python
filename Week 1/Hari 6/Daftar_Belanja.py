belanja = []

jumlah = int (input("Jumlah Barang :"))

for i in range(jumlah):
    barang = input("Nama Barang :")
    belanja.append(barang)

print("===== DAFTAR BELANJA =====")

for i in range (len(belanja)) :
    print (i+1, (belanja[i]))

hapus = input("Apakah ingin menghapus barang ? (Y/N) : ")

if hapus == "y":
    barang_hapus = input("Masukkan nama barang yang akan dihapus :")
    belanja.remove(barang_hapus)
    print("===== Daftar Belanja Yang Baru =====")

    for i in range(len(belanja)):
        print (i+1, belanja[i])