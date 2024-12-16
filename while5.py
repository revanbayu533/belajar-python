n = int(input("Masukkan bilangan: "))
faktorial = 1
i = 1
while i <= n:
    faktorial *= i
    i += 1
print("Faktorial dari", n, "adalah", faktorial)
