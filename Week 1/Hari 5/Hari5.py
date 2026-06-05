#Penggunaan Function
def salam ():
    print ("Selamat Datang")

salam()
salam()
salam()
print()

#Struktur Function
#def nama_fungsi():
#    print ("Isi Fungsi")

def halo ():
    print ("Halo Farhan")

halo()
halo()
print()

#Function dengan Parameter
def halo(nama):
    print(f"Halo {nama}")

halo ("farhan")
print()

def halo(nama, umur):
    print(f"Halo {nama} Umur kamu {umur}")

halo ("farhan", 25)
print()

#Penggunaan Return
def tambah (a, b):
    return a + b

hasil = tambah (10, 5)
print(hasil)
print()

#Function menghitung luas persegi
def luas_persegi (sisi):
    return sisi * sisi

hasil  = luas_persegi (6)

print("hasil luasnya adalah =", hasil)
print()

#Function menghitung BMI
def hitung_bmi (berat, tinggi):
    return berat / (tinggi ** 2)

bmi = hitung_bmi(72, 1.69)

print (bmi)
print()

#Function dengan if
def cek_kalkulator(nilai):
    if nilai >= 75:
        return "lulus"
    else :
        return "Tidak Lulus"

nilai = cek_kalkulator(80)

print(nilai)
print()

#Beberapa function dalam satu program
def tambah (a, b):
    return a + b

def kali (a, b):
    return a * b

print (tambah (5, 10))
print (kali (5, 10))
print()