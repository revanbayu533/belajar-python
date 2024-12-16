def jumlah_elemen(list_angka):
    return sum(list_angka)

list_angka = input("Masukkan daftar angka, pisahkan dengan spasi: ")
list_angka = list(map(int, list_angka.split()))

print("Jumlah elemen dalam daftar adalah:", jumlah_elemen(list_angka))