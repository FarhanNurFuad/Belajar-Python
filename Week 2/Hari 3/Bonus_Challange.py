belanja = []

while True:
    try:
        jumlah = int(input("Jumlah barang: "))
        break
    except ValueError:
        print("Jumlah barang harus angka!")

for i in range(jumlah):
    barang = input(f"Nama barang ke-{i+1}: ")
    belanja.append(barang)

print("\n===== DAFTAR BELANJA =====")
for i, barang in enumerate(belanja, start=1):
    print(f"{i}. {barang}")

hapus = input("\nApakah ingin menghapus barang? (y/n): ").lower()

if hapus == "y":
    barang_hapus = input("Masukkan nama barang yang ingin dihapus: ")

    try:
        belanja.remove(barang_hapus)
        print("\nBarang berhasil dihapus.")
    except ValueError:
        print("\nBarang tidak ditemukan.")

print("\n===== DAFTAR BELANJA TERBARU =====")
for i, barang in enumerate(belanja, start=1):
    print(f"{i}. {barang}")