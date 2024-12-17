kata = input("Masukkan Kalimat : ")
fre = {}

for x in kata:
    if x in fre:
        fre[x] += 1
    else:
        fre[x] = 1

print("Frekuensi karakternya adalah :", fre)