import time
import matplotlib.pyplot as plt

def rek (n):
    if n == 1:
        return 1
    if n > 1:
        return rek(n-1) * (n + 2)

def iter (n):
    k1 = 1
    if n == 1:
        return 1
    if n > 1:
        for i in range(2, n + 1):
            k1 = k1 * (i + 2)
        return k1

while True:
    n = input('введите число n: ')
    if n.isdigit() == True:
        n = int(n)
        break

while True:
    wag = input('Введите шаг изменения числа: ')
    if wag.isdigit() == True:
        wag = int(wag)
        break

n_values = list(range(1, n + 1, wag))

iter_times = []
iter_values = []
rek_times = []
rek_values = []
table = []

for i in n_values:
    start = time.perf_counter()
    iter_values.append(iter(i))
    all_time = time.perf_counter() - start
    iter_times.append(all_time)
    start = time.perf_counter()
    rek_values.append(rek(i))
    all_time = time.perf_counter() - start
    rek_times.append(all_time)

for i, n in enumerate(n_values):
    table.append([n, rek_times[i], iter_times[i], rek_values[i], iter_values[i]])
print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)','Значение рекурсии', 'Значение итерации'))
print('-' * 110)
for data in table:
    print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(data[0], data[1], data[2], data[3], data[4]))


plt.plot(n_values, iter_times, label='итерация')
plt.plot(n_values, rek_times, label='рекурсия')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.legend()
plt.show()