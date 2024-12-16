def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Masukkan bilangan: "))

if is_prime(n):
    print(n, "adalah bilangan prima.")
else:
    print(n, "bukan bilangan prima.")
