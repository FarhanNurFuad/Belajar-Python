nama = input("Nama : ")
umur = input("Umur : ")
kota = input("Kota : ")

mahasiswa = {
    "nama": nama,
    "umur": umur,
    "kota": kota
}

print("\n===== DATA MAHASISWA =====")

for key, value in mahasiswa.items():
    print(key, ":", value)