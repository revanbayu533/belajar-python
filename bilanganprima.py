n = 30
for num in range(2, n + 1):
    for y in range(2, int(num**0.5) + 1):
        if num % y == 0:
            break
    else:
        print(num)   