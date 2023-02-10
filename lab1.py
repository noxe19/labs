d1 = dict([("одна", 1), ("две", 2), ("ноль", 0), ("нуль", 0), ("один", 1), ("два", 2), ("три", 3), ("четыре", 4), ("пять", 5), ("шесть", 6), ("семь", 7),
("восемь", 8), ("девять", 9), ("десять", 10,), ("одиннадцать", 11), ("двенадцать", 12), ("тринадцать", 13), ("четырнадцать", 14),
("пятнадцать", 15), ("шестнадцать", 16), ("семнадцать", 17), ("восемнадцать", 18), ("девятнадцать", 19), ("двадцать", 20),
("тридцать", 30), ("сорок", 40), ("пятьдесят", 50), ("шестьдесят", 60), ("семьдесят", 70), ("восемьдесят", 80), ("девяносто", 90),
("сто", 100), ("двести", 200), ("триста", 300), ("четыреста", 400), ("пятьсот", 500), ("шестьсот", 600), ("семьсот", 700),
("восемьсот", 800), ("девятьсот", 900), ("тысяча", 1000)])

ths = ['тысяча', 'тысячи', 'тысяч']


with open('test(lab1).txt', "r", encoding="utf-8") as file:
    for line in file:
        number_s = line.rstrip()
#        print(number_s)

        arr_num = number_s.lower().split(' ')

        arr_mod = []

        def f(arr):
            summ = 0
            for i in arr:
                summ += d1[i]
            return summ

        if 'тысяча' in arr_num or 'тысячи' in arr_num or 'тысяч' in arr_num:
            sum_ths = 0
            for i in arr_num:
                if i in ths:
                    for j in range(arr_num.index(i)+1, len(arr_num)):
                        arr_mod.append(arr_num[j])
                    break
                if (i in ths) == False:
                    sum_ths += d1[i]
            number = str(f(arr_mod) + sum_ths * 1000)
        else:
            number = str(f(arr_num))

        k = 1

        if len(number) > 1:
            for i in range(0, len(number)-1):
                if number[i] != number[i+1]:
                    k=0
        else:
            k=0

        if k == 1:
            print("1"*120)

        else:
            print(number[::-1])
        print('\n')