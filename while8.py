kalimat = input("Masukkan kalimat: ")
jumlah_kata = 0
i = 0
while i < len(kalimat):
    if kalimat[i] == ' ':
        jumlah_kata += 1
    i += 1
jumlah_kata += 1 
print("Jumlah kata dalam kalimat adalah:", jumlah_kata)
