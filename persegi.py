print('='*40)
print('\t luas persegi')
print('='*40)
def persegi():
    sisi = int(input('Masukkan nilai sisi\t: '))
    luas = lambda sisi : sisi * sisi

    print("Luas persegi =",luas(sisi))

persegi()
persegi()