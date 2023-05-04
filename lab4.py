'''
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных
по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для отладки использовать не случайное заполнение, а целенаправленное. Вид матрицы А:

Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib

10.	Формируется матрица F следующим образом: скопировать в нее А и если в С количество минимальных
чисел в нечетных столбцах, чем количество максимальных чисел в четных строках, то поменять местами
В и С симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После
чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение:
A-1*A – K * F, иначе вычисляется выражение (AТ +GТ-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
'''


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

K = int(input('введите число K: '))
N = int(input('введите число N: '))

A = np.array([[random.randint(-10, 10) for i in range(N)]for j in range(N)])
print('матрица A\n' ,A, '\n')
F = A.copy()

min_element = A.min()
max_element = A.max()

print('матрица F\n', F, '\n')

B, C, E = [], [], []
if N % 2 == 0:
    B = F[0: N // 2, 0: N // 2].copy()
    C = F[0: N // 2, N // 2: N].copy()
    E = F[N // 2: N, N // 2: N].copy()
else:
    B = F[0: N // 2, 0: N // 2].copy()
    C = F[0: N // 2, N // 2 + 1: N].copy()
    E = F[N // 2 + 1: N, N // 2 + 1: N].copy()

k1 = 0
k2 = 0
for i in range(len(B)):
    if i % 2 == 0:
        for j in B[0: len(B), i]:
            if j == min_element:
                k1 += 1
    else:
        for j in B[i, 0: len(B)]:
            if j == max_element:
                k2 += 1

if k1 > k2:
    for i in range(N // 2):
        for j in range(1, N // 2 + 1):
            F[i][j - 1], F[i][-j] = F[i][-j], F[i][j - 1]
else:
    if N % 2 == 0:
        F[0: N // 2, N // 2: N] = E
        F[N // 2: N, N // 2: N] = C
    else:
        F[0: N // 2, N // 2 + 1: N] = E
        F[N // 2 + 1: N, N // 2 + 1: N] = C
print(F, '\n')
print('решение выражения\n')
if np.linalg.det(A) > sum(np.diagonal(F)) + sum(np.diagonal(np.fliplr(F))):
    print(np.linalg.inv(A) * A - K * F)
else:
    print(K * (np.transpose(A) + np.transpose(np.tril(A)) - np.linalg.inv(F)))

plt.plot(F)
plt.title('график 1')
plt.show()
plt.hist(F)
plt.title('график 2')
plt.show()

F_symbol = []
F_quanty_symbol = []
for i in range(-10, 11):
    F_symbol.append(str(i))
    k = 0
    for j in F:
        for j1 in j:
            if j1 == i:
                k += 1
    F_quanty_symbol.append(k)
plt.pie(F_quanty_symbol, labels=F_symbol)
plt.title('график 3')
plt.show()