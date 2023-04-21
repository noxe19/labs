'''С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по
размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.

10.	Формируется матрица F следующим образом: если в С количество минимальных чисел в нечетных
столбцах в области 2 больше, чем количество максимальных чисел в четных строках в области 1,
то поменять в С симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: A*А+(K*AT). Выводятся по
мере формирования А, F и все матричные операции последовательно.
'''


from random import randint
import copy

while True:
    kk = input('введите число k: ')
    n = input('введите число n: ')
    if n.isdigit() == True and kk.isdigit() == True:
        kk = int(kk)
        n = int(n)
        if n >= 5:
            break

''' # закомментировать если нужен ручной ввод
A = [[int(input('введите значение элемента')) for i in range(n)] for i in range(n)]
#''' # раскомментировать если нужен ручной ввод
A = [[randint(-10,10) for j in range(n)] for i in range(n)]
#'''

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print("%5d" % j, end=' ')
        print()
    print('\n')

arr_buffer1 = []
arr_buffer2 = []
max_e = 0
min_e = 0
for i in A:
    for j in i:
        if min_e > j:
            min_e = j
        if max_e < j:
            max_e = j

C, E, C1 = [], [], []
print_matrix(A)
if n % 2 == 0:
    for i in C, E, C1:
        for j in range(n//2):
            i.append([])

    for i in range(n // 2):
        for j in range(n // 2, n):
            C[i].append(A[i][j])
    for i in range(n//2, n):
        for j in range(n // 2, n):
            E[i-n//2].append(A[i][j])

if n % 2 == 1:
    for i in C, E, C1:
        for j in range(n//2+1):
            i.append([])

    for i in range(n // 2 + 1):
        for j in range(n // 2, n):
            C[i].append(A[i][j])
    for i in range(n//2, n):
        for j in range(n // 2, n):
            E[i-n//2].append(A[i][j])

C1 = copy.deepcopy(C)
print('C')
print_matrix(C)
A_copy = copy.deepcopy(A)
At = copy.deepcopy(A)

F = copy.deepcopy(A)

c1 = 0
c2 = 0

def f_mat (flag, ind, c1):
    k = 1
    if n % 4 == 1 or n % 4 == 2:
        for j in range(n // 2 + 1):
            for i in range(0, k):
                arr_buffer1.append(C[i][j])
                if (j + 1) % 2 == 1:
                    if C[i][j] == min_e:
                        c1 += 1
                if flag == 1:
                    C[i][j] = arr_buffer2[ind]
                    ind += 1
            if j >= n // 4:
                k -= 1
            else:
                k += 1
    elif n % 4 == 3:
        for j in range(n // 2 + 1):
            for i in range(0, k):
                arr_buffer1.append(C[i][j])
                if (j + 1) % 2 == 1:
                    if C[i][j] == min_e:
                        c1 += 1
                if flag == 1:
                    C[i][j] = arr_buffer2[ind]
                    ind += 1
            if j == n // 4:
                continue
            elif j > n // 4 - 1:
                k -= 1
            else:
                k += 1
    else:
        for j in range(n // 2):
            for i in range(0, k):
                arr_buffer1.append(C[i][j])
                if (j + 1) % 2 == 1:
                    if C[i][j] == min_e:
                        c1 += 1
                if flag == 1:
                    C[i][j] = arr_buffer2[ind]
                    ind += 1
            if j == n // 4 - 1:
                continue
            elif j > n // 4 - 1:
                k -= 1
            else:
                k += 1
    return c1, arr_buffer1
ind = 0
f_mat(0, 0, 0)

print('C1')
k = 1
if n % 4 != 0 and n % 4 != 3:
    for i in range(n // 2 + 1):
        for j in range(k):
            arr_buffer2.append(C[i][j])
            if (i + 1) % 2 == 0:
                if C[i][j] == max_e:
                    c2 += 1
            C[i][j] = arr_buffer1[ind]
            ind += 1
        if i < n // 4:
            k += 1
        else:
            k -= 1

elif n % 4 == 3:
    for i in range(n // 4 + 1):
        for j in range(k):
            arr_buffer2.append(C[i][j])
            if (i + 1) % 2 == 0:
                if C[i][j] == max_e:
                    c2 += 1
            C[i][j] = arr_buffer1[ind]
            ind += 1
        k += 1
    k -= 1
    for i in range(n // 4 + 1, n // 2 + 1):
        for j in range(k):
            arr_buffer2.append(C[i][j])
            if (i + 1) % 2 == 0:
                if C[i][j] == max_e:
                    c2 += 1
            C[i][j] = arr_buffer1[ind]
            ind += 1
        k -= 1
else:
    for i in range(n // 4):
        for j in range(k):
            arr_buffer2.append(C[i][j])
            if (i + 1) % 2 == 0:
                if C[i][j] == max_e:
                    c2 += 1
            C[i][j] = arr_buffer1[ind]
            ind += 1
        k += 1
    k -= 1
    for i in range(n // 4, n // 2):
        for j in range(k):
            arr_buffer2.append(C[i][j])
            if (i + 1) % 2 == 0:
                if C[i][j] == max_e:
                    c2 += 1
            C[i][j] = arr_buffer1[ind]
            ind += 1
        k -= 1

c1, arr_buffer1 = f_mat(1, 0, 0)
print_matrix(C)

buffer_C = []
for i in C:
    for j in i:
        buffer_C.append(j)

ind = 0

if c1 > c2:
    if n % 4 == 1 or n % 4 == 3:
        for i in range(0, n // 2 + 1):
            for j in range(n // 2, n):
                F[i][j] = buffer_C[ind]
                ind += 1
    if n % 4 == 2 or n % 4 == 0:
        for i in range(0, n // 2):
            for j in range(n // 2, n):
                F[i][j] = buffer_C[ind]
                ind += 1
else:
    buffer_C = []
    for i in C1:
        for j in i:
            buffer_C.append(j)
    buffer_E = []
    for i in E:
        for j in i:
            buffer_E.append(j)
    if n % 2 == 1:
        for i in range(-(n // 2 + 1), 0, 1):
            buffer_C.pop(i)
        for i in range(0, n // 2 + 1):
            buffer_E.pop(0)
        ind = 0
        for i in range(0, n // 2):
            for j in range(n // 2, n):
                F[i][j] = buffer_E[ind]
                ind += 1
        ind = 0
        for i in range(n // 2 + 1, n):
            for j in range(n // 2, n):
                F[i][j] = buffer_C[ind]
                ind += 1
    if n % 2 == 0:
        ind = 0
        for i in range(0, n // 2):
            for j in range(n // 2, n):
                F[i][j] = buffer_E[ind]
                ind += 1
        ind = 0
        for i in range(n // 2, n):
            for j in range(n // 2, n):
                F[i][j] = buffer_C[ind]
                ind += 1

print('F\n')
print_matrix(F)

for i in range(n):
    for j in range(n):
        At[j][i] = A[i][j]
print('Aт\n')
print_matrix(At)

for i in range(n):
    for j in range(n):
        A_copy[i][j] = A[i][j] ** 2

print('A * A\n')
print_matrix(A_copy)

for i in range(n):
    for j in range(n):
        At[i][j] = At[i][j] * kk

print('K * Aт\n')
print_matrix(At)

for i in range(n):
    for j in range(n):
        A_copy[i][j] = A_copy[i][j] + At[i][j]

print('A * A + (K * Aт)')
print_matrix(A_copy)
