#Penggunaan IF

hujan = True

if hujan:
    print ("Bawa Payung")

umur = 20

if umur >= 17:
    print ("Boleh Membuat SIM")

nilai = 80
print (nilai >= 75)
print()

#Penggunaan if else
umur = 15

if umur >= 17:
    print ("Boleh Membuat SIM")
else:
    print("Tidak boleh membuat SIM")
print()

#Pengunaan imput dan if
umur = int(input("Masukan Umur :"))

if umur >= 17:
    print ("Boleh Membuat SIM")
else:
    print("Tidak boleh membuat SIM")
print()

#Pengunaan if elif else
nilai = 85

if nilai >= 95:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print ("C")
else :
    print ("D")
print()

#Program Penilaian Mahasiswa
nilai = int(input("Masukan nilai :"))

if nilai >= 95:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else :
    grade = "D"

print ("Nilai kamu adalah =", grade)
print()

#Operator Logika AND dan OR
# AND = Semua harus Benar
# OR = Salah Satu Benar

#contoh AND
umur = 30
punya_ktp = True

if umur >= 17 and punya_ktp:
    print ("Boleh membuat SIM")

#Contoh OR
user = "admin"
email = "admin@thredio.com"

if user == "admin" or email == "admin@thredio.com":
    print("Login Berhasil")

#Login Sederhana
user = input("Masukan Username :")
password = input("Masukkan Password :")

if user == "admin" and password == "12345":
    print("Login Berhasil")
else :
    print("Login Gagal")