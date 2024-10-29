print('='*40)
print('\t luas layang-layang')
print('='*40)

def layang_layang():
    d1 = int(input('Masukkan panjang d1:'))
    d2 = int(input('Masukkan panjang d2:'))
    luas = lambda d1,d2: 0.5 * d1 * d2 
    print('luas layang_layang=',luas(d1,d2))

layang_layang()
layang_layang()