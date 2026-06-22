angka1 = float(input("Angka pertama: "))
angka2 = float(input("Angka kedua: "))


def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    return a / b

print (f"Penjumlahan ={tambah(angka1, angka2)}")
print (f"Pengurangan ={kurang(angka1, angka2)}")
print (f"Perkalian ={kali(angka1, angka2)}")
print (f"Pembagian ={bagi(angka1, angka2)}")