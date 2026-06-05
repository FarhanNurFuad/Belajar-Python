def hitung_bmi (berat, tinggi):
    return berat / (tinggi ** 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else :
        return "Obesitas"

bmi = hitung_bmi(72, 1.69)

print (bmi)
print (kategori_bmi(bmi))