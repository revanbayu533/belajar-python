bulan1 = ["Februari", "Januari", "Mei"]
bulan2 = ["Maret", "April", "Juni", "Juli","November","Desember"]
bulan3 = ["September", "Agustus", "Oktober"]
print("Bulan Langka \t:")
for r,t in enumerate(bulan1):
    print(r+1,'.',t)
print("Bulan Umum \t:")
for o,q in enumerate(bulan2):
    print(o+1,'.',q)
print("Bulan Populer \t:")
for p,d in enumerate(bulan3):
    print(p+1,'.',d)