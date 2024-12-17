import math
angka_pertama = int(input("Tulis angka pertama: "))
angka_kedua = int(input("Tulis angka kedua: "))
fpb = math.gcd(angka_pertama, angka_kedua)
kpk = (angka_pertama * angka_kedua) // fpb
print(f"FPB dari {angka_pertama} dan {angka_kedua} = {fpb}")
print(f"KPK dari {angka_pertama} dan {angka_kedua} = {kpk}")