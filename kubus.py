print('='*40)
print('\t luas permukaan kubus')
print('='*40)
def kubus():
    sisi = float(input('Masukkan panjang sisi kubus:'))
    luas_permukaan = lambda sisi: 6 * (sisi ** 2)
    print('luas permukaan kubus =',luas_permukaan(sisi))

kubus()
kubus()