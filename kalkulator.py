def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol"

def kalkulator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan bilangan pertama: "))
    num2 = float(input("Masukkan bilangan kedua: "))

    if pilihan == '1':
        print("Hasil:", tambah(num1, num2))
    elif pilihan == '2':
        print("Hasil:", kurang(num1, num2))
    elif pilihan == '3':
        print("Hasil:", kali(num1, num2))
    elif pilihan == '4':
        print("Hasil:", bagi(num1, num2))
    else:
        print("Pilihan tidak valid")

kalkulator()