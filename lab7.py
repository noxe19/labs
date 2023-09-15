'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы)
написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода

№6
2 часть – усложнить написанную программу, введя по своему усмотрению в
условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
(вывести все числа с максимальной суммой цифр в интервалах от 0 до 100, от 100 до 200 и т.д.)

Вариант 10. Вывести все натуральные числа до n, в записи которых встречается от 2 до 3 четных цифр.
'''


class number:
    counter_num = 0

    def __init__(self, num, sum_digits, even_digits):
        self.num = num
        self.sum_digits = sum_digits
        self.even_digits = even_digits

    def show_counter_num(self):
        print("\nколличество выведенных чисел:", number.counter_num)

    def show_num(self):
        print(self.num)
        number.counter_num += 1


sbl = ['0', '2', '4', '6', '8']

while True:
    n = input("Введите любое натурально число, которое больше 19: ")
    if n.isdigit():
        n = int(n)
        break


buf_num = 0
buf_sum = 0
buf_i = 0
for i in range(20, n + 1):
    k = 0
    summ = 0
    for j in str(i):
        if j in sbl:
            summ += int(j)
            k += 1

    num_obj = number(i, summ, k)
    if num_obj.even_digits >= 2:
        if i // 100 > buf_i:
            buf_i += 1
            print(buf_num)
            buf_sum = 0
            buf_num = 0
        elif buf_sum < num_obj.sum_digits:
            buf_sum = num_obj.sum_digits
            buf_num = num_obj.num
    if i == n:
        print(buf_num)

num_obj.show_counter_num()