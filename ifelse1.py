print("="*40)
print("NILAI SISWA SMP")
print("="*40)

nama_siswa_smp = input('Masukkan nama siswa smp:')
nilai = int(input('Masukkan nilai siswa smp:'))

if 90 <= nilai <= 100:
    grade = 'A'
elif 80 <= nilai <= 89:
    grade = 'B'
elif 60 <= nilai <= 79:
    grade = 'C'
elif 40 <= nilai <= 59:
    grade = 'D'
else:
    grade = 'E'

print(f"Nama Siswa SMP: {nama_siswa_smp}")
print(f"Nilai: {nilai}")
print(f"Grade: {grade}")