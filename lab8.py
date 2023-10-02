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
from tkinter.ttk import Progressbar


sbl_arr = ['0', '2', '4', '6', '8']


def input_number(event):
    n = ent.get()

    if n.isdigit():
        if int(n) < 20:
            n = int(ent.get())
            lab.configure(text="Введите целое, положительное число, больше 19")
        else:
            calculations(int(n))
    else:
        lab.configure(text="Введите целое, положительное число, больше 19")


def suitable_number(i):
    k = 0
    summ = 0
    for j in str(i):
        if j in sbl_arr:
            summ += int(j)
            k += 1
    return k, summ


def calculations(n):
    progress = 0
    progress_buf = 0
    if n > 200000000:
        step = n // 1000
        progress_step = 1
    else:
        step = n // 100
        progress_step = 10
    progress_bar['value'] = progress
    lab_info.configure(text="Ждите")
    root.update()

    arr = ''

    output = Tk()
    output.title("окно вывода")
    output.geometry("400x200")

    output_lab = Label(output, text="вывод")
    st = ScrolledText(output)
    output_lab.pack(pady=10)

    buf_num = 0
    buf_sum = 0
    buf_i = 0
    for i in range(20, n + 1):
        if i == progress_buf + step:
            progress_buf += step
            progress += progress_step
            progress_bar['value'] = progress
            root.update()
        k, summ = suitable_number(i)
        if 1 < k < 4:
            if i // 100 > buf_i:
                buf_i += 1
                arr += str(buf_num) + "\n"
                buf_sum = 0
                buf_num = 0
            elif buf_sum < summ:
                buf_sum = summ
                buf_num = i
        if i == n:
            arr += str(buf_num) + "\n"

    st.insert("1.0", arr)
    st.configure(state='disabled')
    lab_info.configure(text="Готово")
    st.pack()


def info_window():
    info = Tk()
    info.title("окно информации")
    info.geometry("500x200")

    info_lab = Label(info, text="Выводит все натуральные числа до n,\n с максимальной суммой цифр в интервалах от 0 до 100, от 100 до 200 и т.д.,\n в записи которых встречается от 2 до 3 четных цифр.")

    info_but = Button(info, text="Ок", command=info.destroy)
    info_lab.pack(pady=20)
    info_but.pack()


info_window()

root = Tk()
root.title("окно ввода")
root.geometry("400x200")

lab = Label(root, text="Введите любое натурально число, которое больше 19:")
ent = Entry(root, width=20)
but = Button(root, text="Преобразовать")
lab_info = Label(root, text="программа готова к работе")
progress_bar = Progressbar(root, orient="horizontal", mode="determinate", maximum=1000, value=0)

lab.pack(side=TOP, pady=5)
ent.pack()
but.pack(pady=10)
progress_bar.pack(pady=20, side=BOTTOM, fill=X)
lab_info.pack(side=BOTTOM)

but.bind('<Button-1>', input_number)

root.mainloop()
