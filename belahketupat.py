print('='*40)
print('\t luas belah ketupat')
print('='*40)

def belah_ketupat():
    d1 = int(input('Masukkan panjang d1:'))
    d2 = int(input('Masukkan panjang d2:'))
    luas = lambda d1,d2: 0.5 * d1 * d2
    print('luas belah_ketupat=',luas(d1,d2))

belah_ketupat()
belah_ketupat()