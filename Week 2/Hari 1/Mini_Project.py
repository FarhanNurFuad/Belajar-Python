username = input("Masukkan username: ")

if len(username) < 5:
    print("Username tidak valid, minimal 5 karakter")
elif " " in username:
    print("Username tidak valid, tidak boleh mengandung spasi")
else:
    print("Username valid")