print("="*40)
print("NAMA BULAN DALAN KALENDER")
print("="*40)

nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
"Juli", "Agustus", "September", "Oktober", "November", "Desember"]

nomor_bulan = int(input("Masukkan nomor bulan (1-12): "))

if 1 <= nomor_bulan <= 12 :
    print("Nama bulan:", nama_bulan[nomor_bulan - 1])
else:
    print("Nomor bulan tidak valid. Silahkan masukkan angka antara 1 dan 12. ")