count = int(input("반복할 횟수: "))
for n in range (1, count + 1):
    if n % 2 != 0:
        continue
    print(n)