print('=' * 40)
print('SUKA ATAU TIDAK MIE AYAM')
print('=' * 40)

def mie_ayam():
    jawaban = input("Apakah Anda suka mie ayam? (ya/tidak): ").lower()
    if jawaban == "ya":
        print("Keren! Mie ayam memang lezat.")
    elif jawaban == "tidak":
        print("Oh, sayang sekali! Mungkin ada makanan lain yang lebih Anda suka.")
    else:
        print("Jawaban tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")

mie_ayam()