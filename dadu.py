import random

def lempar_dadu():
    return random.randint(1, 6)

jumlah_lemparan = int(input("Masukkan jumlah lemparan dadu: "))

for i in range(jumlah_lemparan):
    hasil = lempar_dadu()
    print(f"Lemparan ke-{i+1}: {hasil}")
