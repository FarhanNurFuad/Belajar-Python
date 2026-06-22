data = input("Masukkan biodata (nama,umur,kota): ")

hasil = data.split(",")

nama = hasil[0].strip().title()
umur = hasil[1].strip()
kota = hasil[2].strip().title()

print("\n===== BIODATA =====")
print(f"Nama : {nama}")
print(f"Umur : {umur}")
print(f"Kota : {kota}")