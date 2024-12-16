print("="*40)
print("TIGA BILANGAN BULAT")
print("="*40)

def urutkan_tiga_bilangan(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b 
    if a > b:
        a, b = b, a 
    return a, b, c, 
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

terurut = urutkan_tiga_bilangan(bilangan1, bilangan2, bilangan3)

print("Bilangan terurut dari kecil ke besar adalah:", terurut)