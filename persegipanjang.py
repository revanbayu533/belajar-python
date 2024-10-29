print('='*40)
print('\t luas persegi panjang')
print('='*40)

def persegi_panjang():
    panjang = int(input('Masukkan nilai panjang: '))
    lebar = int(input('Masukkan nilai lebar : '))
    
    luas = lambda panjang,lebar: panjang * lebar
    print('luas persegi_panjang =', luas(panjang,lebar))

persegi_panjang()
persegi_panjang()