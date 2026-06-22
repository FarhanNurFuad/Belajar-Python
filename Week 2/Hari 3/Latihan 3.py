while True:
    try:
        umur = int(input("Masukkan umur: "))
        print("Umur kamu:", umur)
        break
    except ValueError:
        print("Input salah, masukkan angka!")