print("="*40)
print("MASA SESEORANG")
print("="*40)

nama = input("Masukkan Nama:")
usia = int(input("Masukkan Usia:"))

if 65 <= usia <= 79:
    masa = 'Dewasa Tua'
elif 45 <= usia <= 64:
    masa = 'Dewasa Madya'
elif 20 <= usia <=44 :
    masa = 'Dewasa Muda'
elif 15 <= usia <= 19:
    masa = 'Remaja'
elif 9 <= usia <= 14:
    masa = 'Kanak-Kanak'
elif 1 <= usia <= 8:
    masa = 'Kehidupan Awal'
else:
    masa = 'Panjang usia'

print(f'Nama: {nama}')
print(f"Usia: {usia}")
print(f"Masa: {masa}")