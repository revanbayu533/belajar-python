angka = int(input("Masukkan bilangan: "))
jumlah_digit = 0
while angka > 0:
    angka //= 10
    jumlah_digit += 1
print("Jumlah digit dalam bilangan adalah:", jumlah_digit)
