# Meminta input dua bilangan dari pengguna
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Menentukan bilangan terbesar dengan statement if
if bilangan1 > bilangan2:
    terbesar = bilangan1
else:
    terbesar = bilangan2

# Menampilkan bilangan terbesar
print("Bilangan terbesar adalah:", terbesar)
