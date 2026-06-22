def hitung_diskon(harga):
    if harga >= 100000:
        return harga - (0.1*harga)
    else :
        return harga

print(hitung_diskon(150000))