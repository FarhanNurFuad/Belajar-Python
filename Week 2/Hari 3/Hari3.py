#Try_Except
umur = int(input("Masukkan umur: "))
print("Umur:", umur)
print()

#Dasar Try-Except
try:
    umur = int(input("Masukkan umur: "))
    print("Umur:", umur)
except:
    print("Input harus berupa angka!")
print()

#Try-Except dengan Error Tertentu
try:
    umur = int(input("Masukkan umur: "))
    print("Umur:", umur)
except ValueError:
    print("Input harus angka!")
print()

#Menangani Pembagian Nol
try:
    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))

    hasil = angka1 / angka2
    print("Hasil:", hasil)

except ZeroDivisionError:
    print("Tidak bisa dibagi dengan 0!")

except ValueError:
    print("Input harus angka!")
print()

#Else pada Try-Except
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input harus angka!")
else:
    print("Input berhasil:", angka)
print()

#Finally
try:
    angka = int(input("Masukkan angka: "))
    print(angka)
except ValueError:
    print("Input harus angka!")
finally:
    print("Program selesai.")
print()

#Try-Except di Dalam Loop
while True:
    try:
        umur = int(input("Masukkan umur: "))
        print("Umur:", umur)
        break
    except ValueError:
        print("Input salah, masukkan angka!")
print()

#Try-Except + Function
def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("Input harus angka!")

angka1 = input_angka("Masukkan angka pertama: ")
angka2 = input_angka("Masukkan angka kedua: ")

print("Hasil penjumlahan =", angka1 + angka2)
print()

#Menangani Error Saat Menghapus Barang dari List
belanja = ["Beras", "Gula", "Minyak"]

barang = input("Masukkan barang yang ingin dihapus: ")

try:
    belanja.remove(barang)
    print("Barang berhasil dihapus")
except ValueError:
    print("Barang tidak ditemukan")
print()

#Menangani IndexError
buah = ["Apel", "Jeruk", "Mangga"]

try:
    index = int(input("Masukkan index: "))
    print(buah[index])
except IndexError:
    print("Index tidak tersedia!")
except ValueError:
    print("Input index harus angka!")