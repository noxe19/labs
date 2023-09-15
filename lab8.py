"""
Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной
реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать
любую графическую библиотеку питона.  Рекомендуется использовать внутреннюю библиотеку питона  tkinter.

В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.

№6
2 часть – усложнить написанную программу, введя по своему усмотрению в
условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
(вывести все числа с максимальной суммой цифр в интервалах от 0 до 100, от 100 до 200 и т.д.)

Вариант 10. Вывести все натуральные числа до n, в записи которых встречается от 2 до 3 четных цифр.
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import font


class number:
    counter_num = 0

    def __init__(self, num, sum_digits, even_digits):
        self.num = num
        self.sum_digits = sum_digits
        self.even_digits = even_digits

    def show_counter_num(self):
        print("\nколличество выведенных чисел:", number.counter_num)
        number.counter_num = 0

    def show_num(self):
        number.counter_num += 1
        return self.num


sbl_arr = ['0', '2', '4', '6', '8']


def input_number(event):
    n = ent.get()

    if n.isdigit():
        if int(n) < 20:
            n = int(ent.get())
        else:
            calculations(int(n))


def calculations(n):
    arr = ''

    output = Tk()
    output.title("окно вывода")
    output.geometry("400x200")

    output_lab = Label(output, text="вывод")
    close_button = Button(output, text="Закрыть окно", command=lambda: output.destroy())
    st = ScrolledText(output)

    output_lab.pack()

    buf_num = 0
    buf_sum = 0
    buf_i = 0
    for i in range(20, n + 1):
        k = 0
        summ = 0
        for j in str(i):
            if j in sbl_arr:
                summ += int(j)
                k += 1

        num_obj = number(i, summ, k)
        if num_obj.even_digits >= 2:
            if i // 100 > buf_i:
                buf_i += 1
                arr += (str(buf_num) + "\n")
                number.counter_num += 1
                buf_sum = 0
                buf_num = 0
            elif buf_sum < num_obj.sum_digits:
                buf_sum = num_obj.sum_digits
                buf_num = num_obj.show_num()
        if i == n:
            number.counter_num += 1
            arr += (str(buf_num) + "\n")
    print(arr)


    num_obj.show_counter_num()
    st.insert("1.0", arr)
    st.pack()
    close_button.pack(anchor="center", expand=1)


root = Tk()
root.title("окно ввода")
root.geometry("400x200")

font_txt = font.Font(size=11)
lab = Label(text="Введите любое натурально число, которое больше 19:", font=font_txt)
ent = Entry(width=20)
but = Button(text="Преобразовать")

lab.pack()
ent.pack()
but.pack()

but.bind('<Button-1>', input_number)

root.mainloop()
