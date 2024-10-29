print('='*40)
print('\t luas permukaan bola')
print('='*40)

def bola():
    jari_jari = float(input('Masukkan jari-jari bola:'))
    luas_permukaan = lambda jari_jari: 4 * 3.14 * jari_jari * 2
    print('luas permukaan bola=',luas_permukaan(jari_jari))

bola()
bola()