print('='*40)
print('\t luas permukaan tabung')
print('='*40)

def tabung():
    jari_jari = int(input('Masukkan jari-jari tabung:'))
    tinggi = int(input('Masukkan tinggi tabung:'))
    luas_permukaan = lambda jari_jari,tinggi: 2 * 22/7 * jari_jari * (jari_jari + tinggi)
    print('luas permukaan tabung=',luas_permukaan(jari_jari,tinggi))

tabung()
tabung()