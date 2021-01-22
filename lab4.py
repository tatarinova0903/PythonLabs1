# Вычислить таблицу значений функции и построить её график 
# x1 = 2.97*q**4 + 4.84*q**3 - 16.4*q**2 + 41.2*q - 33.2
# x2 = 2 - q*exp(q)
# Татаринова Дарья ИУ-14Б

from math import exp

eps = 1e-10

# Ввод данных
start, end, h = map(float, input("Введите начало, конец интервала и шаг: ").split())

count = round((end - start)/h + 1) #количество возможных значений q
x1 = [0]*count #массив для записи значений функции x1
x2 = [0]*count #массив для записи значений функции x2

# Вывод заголовка таблицы
print ("{:^10}{:^11}{:^11}".format("q", "x1", "x2"))

# Заполнение массивов значениями функций в данных точках, поиск максимумов функций
q = start
x1_max = x1_min = 2.97*q**4 + 4.84*q**3 - 16.4*q**2 + 41.2*q - 33.2
x2_max = x2_min = 2 - q*exp(q)
index = 0
intersection_with_Ox = 0
while q < end or abs(q - end) < eps:
    x1[index] = 2.97*q**4 + 4.84*q**3 - 16.4*q**2 + 41.2*q - 33.2
    x2[index] = 2 - q*exp(q)
    if x1[index] > x1_max:
        x1_max = x1[index]
    if x2[index] > x2_max:
        x2_max = x2[index]
    if x1[index] < x1_min:
        x1_min = x1[index]
    if x2[index] < x2_min:
        x2_min = x2[index]
    if index > 0 and x2[index - 1] * x2[index] < 0:
        intersection_with_Ox = 1 # функция x2 пересекает ось Ox
    index += 1
    q += h

# Вывод значений функций в точках
q = start
i = 0
while i < count:
    print ("{:^10.3g}{:^11.3g}{:^11.3g}".format(q, x1[i], x2[i]))
    q += h
    i += 1

# Подсчет разницы максимумов двух функций
x_delta = x1_max - x2_max
print ("\nx1_max - x2_max =", "{:4.3g}".format(x_delta), "\n")


# Построение графика функции x1
z = int(input("Введите количество засечек: "))

z -=1

d = (x1_max - x1_min) / z 
value_of_q = x1_min
print ("    ", end = "")
# Вывод значений на оси x
for i in range(z*19):
    if i == z*19 -1 :
        print("{:^11.4g}".format(x1_max), end = "")
    elif i%19 == 0:
        print("{:^12.4g}".format(value_of_q), end = "")
        value_of_q += d
    elif i == z*19 - 1:
        print ("  ", "{:^11.4g}".format(value_of_q))
    elif i%19 < 19 - 11:
        print (" ", end = "")


# Вывод оси
print()
for i in range(z*19 + 1):  
    if i == 0:
        print("        |", end = "")
    elif i%19 == 0:
        print("|", end = "")
    else:
        print ("-", end = "")
print("\n", end = "")


# Рисование графика
q = start
for i in range (count):
    print ("{:>7.3f}".format(q), end = " ")
    # f = round((z * 19 * abs(x1[i] - x1_min)) / (x1_max + abs(x1_min)))
    # print (abs(x1[i] - x1_min))
    # print (z * 19 * abs(x1[i] - x1_min))
    # print ((z * 19 * abs(x1[i] - x1_min)) / (x1_max + abs(x1_min)))
    for j in range(z * 19 + 1):
        if j == round((z * 19 * abs(x1[i] - x1_min)) / (x1_max + abs(x1_min))):
            print ("*", end = "")
        elif intersection_with_Ox == 1 and j == round(z * 19 * abs(x1_min) / (x1_max + abs(x1_min))):
            print("|", end = "")
        else:
            print(" ", end = "")
    print("")
    q += h
