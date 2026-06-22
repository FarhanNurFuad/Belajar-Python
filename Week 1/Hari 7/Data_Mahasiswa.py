nama = input("Nama : ")
umur = input("Umur : ")
kota = input("Kota : ")
jurusan = input("jurusan : ")

mahasiswa = {
    "nama": nama,
    "umur": umur,
    "kota": kota,
    "jurusan" : jurusan
}

print("\n===== DATA MAHASISWA =====")

for key, value in mahasiswa.items():
    print(key, ":", value)