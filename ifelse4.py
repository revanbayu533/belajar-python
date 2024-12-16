print("="*40)
print(" PANJANG TIGA BUAH SISI SEGITIGA")
print("="*40)

def jenis_segitiga(a, b, c):
    if a**2 + b**2 == c**2:
        return "Segitiga siku-siku"
    elif a**2 + b**2 > c**2:
        return "Segitiga lancip"
    else:
        return "Segitiga tumpul"

a = int(input("Masukkan panjang sisi a (a < b < c): "))
b = int(input("Masukkan panjang sisi b (a < b < c): "))
c = int(input("Masukkan panjang sisi c (a < b < c): "))

if a >= b or b >= c or a >= c:
    print("Masukkan nilai yang memenuhi syarat a < b < c.")
else:
    hasil = jenis_segitiga(a, b, c)
    print(f"Jenis segitiga dengan sisi {a}, {b}, dan {c} adalah: {hasil}")