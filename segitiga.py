print('='*40)
print('\t luas segitiga')
print('='*40)

def segitiga():
    alas = int(input('Masukkan panjang alas:'))
    tinggi = int(input('Masukkan tinggi alas:'))
    luas = lambda alas,tinggi : 0.5 * alas * tinggi 

    print("luas segitiga =",luas(alas,tinggi))

segitiga()