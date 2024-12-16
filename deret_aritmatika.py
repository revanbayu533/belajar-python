print('='*40)
print('DERET ARITMATIKA')
print('='*40)

U1 = int(input('Masukkan U1 :'))
d = int(input('Masukkan d :'))
n = int(input('Masukkan n :'))

def suku_ke_n_aritmatika(U1, d, n):
    Un = U1 + (n - 1) * d
    return Un
 
hasil = suku_ke_n_aritmatika(U1, d, n)
print(f"Suku ke-{n} dari deret aritmatika adalah: {hasil}")