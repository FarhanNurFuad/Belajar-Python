while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        operator = input("Masukkan operator (+, -, *, /): ")

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            hasil = angka1 / angka2
        else:
            print("Operator tidak valid!")
            continue

        print(f"Hasil = {hasil}")
        break

    except ValueError:
        print("Input angka tidak valid, coba lagi!")

    except ZeroDivisionError:
        print("Tidak bisa membagi dengan 0, coba lagi!")