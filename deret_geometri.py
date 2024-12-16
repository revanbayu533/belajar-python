print('='*40)
print('DERET GEOMETRI')
print('='*40)
U1 = int(input('Masukkan U1 :'))
r = int(input('Masukkan r :'))
n = int(input('Masukkan n :'))

def suku_ke_n_geometri(U1, r, n):
    Un = U1 * (r ** (n - 1))
    return Un

hasil = suku_ke_n_geometri(U1, r, n)
print(f"Suku ke-{n} dari deret geometri adalah: {hasil}")