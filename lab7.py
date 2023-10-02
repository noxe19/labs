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


class Number:

    def __init__(self, start_num, end_num, step):
        self.start_num = start_num
        self.end_num = end_num
        self.step = step

    @staticmethod
    def suitable_number(i):
        k = 0
        summ = 0
        for j in str(i):
            if j in sbl:
                summ += int(j)
                k += 1
        return k, summ

    def dk(self):
        buf_num = 0
        buf_sum = 0
        buf_i = 0
        for i in range(self.start_num, self.end_num + 1, self.step):
            k, summ = number.suitable_number(i)
            if 1 < k < 4:
                if i // 100 > buf_i:
                    buf_i += 1
                    print(buf_num)
                    buf_sum = 0
                    buf_num = 0
                elif buf_sum < summ:
                    buf_sum = summ
                    buf_num = i
            if i == n:
                print(buf_num)

sbl = ['0', '2', '4', '6', '8']

while True:
    print("Выводит все натуральные числа до n, с максимальной суммой цифр в интервалах от 0 до 100, от 100 до 200 и т.д.,\n в записи которых встречается от 2 до 3 четных цифр.")
    n = input("Введите любое натурально число 'n', которое больше 19: ")
    if n.isdigit():
        n = int(n)
        if n > 19:
            break

number = Number(20, n, 1)
number.dk()
print("конец работы")
