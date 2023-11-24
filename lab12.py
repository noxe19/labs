"""
10. Вычислить сумму знакопеременного ряда (|х(2n)|)/(2n)!, где х-матрица ранга к
(к и матрица задаются случайным образом), n - номер слагаемого. Сумма считается вычисленной,
если точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная сложность.
Операция умножения –поэлементная. Знак первого слагаемого  +.
"""
from random import randint
from random import uniform
import numpy as np

while True:
    eps = input("До какого знака, после запятой, считать сумму ряда: ")
    if eps.isdigit():
        eps = int(eps)
        if eps > 0:
            break

buf_eps = eps
eps = 1 / (10 ** eps)
print(eps, "\n")

factorial_n = 1
k = randint(1, 10)

matrix = np.array([[uniform(-1, 1) for j in range(k)] for i in range(k)])
result_matrix = matrix.copy()
result = 0
print(matrix, "\n")

buf_sign = 1
result_num = 0
while_stop = False


def matrix_fun(sign, num):
    global result_num
    global while_stop
    if abs(result) > eps:
        if i == 1:
            result_num += abs(num)
        else:
            result_num += num * sign
    else:
        while_stop = True


i = 1
j = 1
buf_j = 1
while True:
    if while_stop:
        break
    n = i * 2
    for c in range(j, n+1):
        factorial_n *= c
        buf_j += 1
    j = buf_j
    result_matrix *= n
    matrix_det = np.linalg.det(result_matrix)
    result_matrix = matrix.copy()
    result = matrix_det / factorial_n
    matrix_fun(buf_sign, result)
    buf_sign *= -1
    print(format(result_num, f'.{buf_eps}f'))
    i += 1


print("\nОтвет: ", format(result_num, f'.{buf_eps}f'))
