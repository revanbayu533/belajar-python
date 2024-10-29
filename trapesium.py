print('='*40)
print('\t luas trapesium')
print('='*40)

def trapesium():
    sisi_atas = int(input('Masukkan panjang sisi sejajar atas:'))
    sisi_bawah = int(input('Masukkan panjang sisi sejajar bawah:'))
    tinggi = int(input('Masukkan tinggi trapesium:'))
    luas = lambda sisi_atas,sisi_bawah,tinggi: 0.5 * (sisi_atas + sisi_bawah) * tinggi
    print('luas trapesium =',luas(sisi_atas,sisi_bawah,tinggi))

trapesium()
trapesium()