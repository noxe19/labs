n = int(input("Введите число: "))

sbl = ['0', '2', '4', '6', '8']

for i in range(1, n + 1):
    k = 0
    for j in str(i):
        if j in sbl:
            k += 1
    if k == 2 or k == 3:
        print(i)
print('\n')
for i in range(1, n + 1):
    k = 0
    if i % 3 % 5 == 0:
        for j in str(i):
            if j in sbl:
                k += 1
    else:
        continue
    if k == 2 or k == 3:
        print(i)

