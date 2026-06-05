mahasiswa_list = []

for i in range(3):
    nama = input("Nama : ")
    umur = input("Umur : ")

mahasiswa = {
    "nama": nama,
    "umur": umur
}

mahasiswa_list.append(mahasiswa)

for mahasiswa in mahasiswa_list:
    for key, value in mahasiswa.items():
        print(key, ":", value)

    print()