import csv

average_age = 0
buf = []
error = 10
count_children = 0
with open('Titanic-Dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        age = row[5]
        if age.isdigit():
            age = int(age)
            if age < 18:
                average_age += age
                buf.append([age, row[1]])
                count_children += 1
        elif age == "":
            buf.append([0, row[1]])
            count_children += 1

count_survived_children = 0
average_age = average_age // count_children
for i in buf:
    if i[0] in range(average_age - error, average_age + error + 1):
        if int(i[1]) == 1:
            count_survived_children += 1

print("Кол-во детей: ", count_children)
print("Кол-во выжевших детей: ", count_survived_children)
