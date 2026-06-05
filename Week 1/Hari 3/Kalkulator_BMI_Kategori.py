user = input("Masukkan Username :")
password = input("Masukan Password :")

if user == "admin" and password == "python123":
    print("===== Selamat datang Admin =====")
else :
    print("Username atau Password salah")
print()

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

bmi = berat / tinggi ** 2

if bmi < 18.5 :
    hasil = "Kurus"
elif bmi < 25 :
    hasil = "Normal"
elif bmi < 30 :
    hasil = "Overweight"
else :
    hasil = "Obesitas"

print ("Hasil BMI kamu adalah :", hasil)
