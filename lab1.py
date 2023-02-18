'''
Написать программу, которая читая символы из бесконечной последовательности
(эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и
выводит на экран числа по определенному правилу. Числа распознаются по законам
грамматики русского языка. Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод
всех цифр числа. Регулярные выражения использовать нельзя.
'''
buffer = ''
buffer_len = 1
work_buffer = ''
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
with open('test(lab1).txt', 'r') as file:
    buffer = file.read(buffer_len)
    while buffer:
        while True:
            if buffer != ' ' and buffer != '\n':
                work_buffer += buffer
            buffer = file.read(buffer_len)
            if buffer == '' or buffer == ' ' or buffer == '\n':
                break
        n1 = 0
        n2 = 0
        for i in work_buffer:
            if i in arr:
                n1 = 1
            else:
                n1 = 0
                break
        if len(work_buffer) > 1:
            for i in range(len(work_buffer)-1):
                if work_buffer[i] == work_buffer[i+1]:
                    n2 = 1
                else:
                    n2=0
                    break
        if n2 == 1 and n1 == 1:
            print('1' * 120)
        elif n1 == 1:
            print(work_buffer[::-1])
        work_buffer = ''
