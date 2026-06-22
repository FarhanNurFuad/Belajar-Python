try:
    angka = int(input("Masukkan angka: "))
    print("Angka yang dimasukkan:", angka)
except ValueError:
    print("Input harus angka!")