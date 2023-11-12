"""
10. Вычислить сумму знакопеременного ряда (|х(2n)|)/(2n)!, где х-матрица ранга к
(к и матрица задаются случайным образом), n - номер слагаемого. Сумма считается вычисленной,
если точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная сложность.
Операция умножения –поэлементная. Знак первого слагаемого  +.
"""
from random import randint
from random import uniform
import numpy as np


k = randint(1, 10)


matrix = np.array([[uniform(-1, 1) for j in range(k)] for i in range(k)])
result_matrix = matrix.copy()
result = 0
print(matrix, "\n")


def matrix_fun(result_matrix, num, divider, sign):
    global result

    result_matrix = result_matrix * 2 * num
    matrix_det = np.linalg.det(result_matrix)
    if sign == "+":
        result += matrix_det / divider
    else:
        result -= matrix_det / divider
    return result


def factorial(num):
    result = 1
    if num == 0:
        return result
    else:
        while num != 1:
            result *= num
            num -= 1
        return result


buf_sign = "+"
result_num = 0
i = 1
while i != 12:
    flag = i
    n = 2 * i
    factorial_n = factorial(n-1)
    result = matrix_fun(result_matrix, n, factorial_n, buf_sign)
    if buf_sign == "+":
        buf_sign = "-"
    else:
        buf_sign = "+"
    i += 1
    print(result)
print("\nОтвет: ", result)

