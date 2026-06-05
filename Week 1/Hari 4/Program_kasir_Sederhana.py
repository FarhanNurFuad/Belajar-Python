jumlah = int(input("Jumlah Barang :"))

total = 0

for i in range(jumlah) :
    harga = int(input(f"Masuhkan Harga barang {i} :"))
    total += harga

print("Total harga barang anda =", total)