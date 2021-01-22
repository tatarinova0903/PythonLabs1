eps = 1e-10

start, end, h = map(float, input("Введите начало, конец интервала и шаг: ").split())

count = round((end - start)/h + 1) 
y = [0]*count 
intersection_with_Oy = 0
x = start
y_min = x**3 - 2*x**2
y_max = x**3 - 2*x**2
for i in range(count):
    y[i] = x**3 - 2*x**2
    if y[i] > y_max:
        y_max = y[i]
    if y[i] < y_min:
        y_min = y[i]
    if i > 0 and (y[i]*y[i - 1] < 0 or y[i]*y[i-1] < eps):
        intersection_with_Oy = 1
    x += h

z = int(input("Введите количество засечек: "))
z -= 1

delta = (y_max - y_min) / z
value_of_x = y_min

print("    ", end = "")
for i in range(z*15):
    if i == z*15 -1 :
        print("{:^11.4g}".format(y_max), end = "")
    elif i%15 == 0:
        print("{:^12.4g}".format(value_of_x), end = "")
        value_of_x += delta
    elif i == z*15 - 1:
        print ("  ", "{:^11.4g}".format(value_of_x))
    elif i%15 < 15 - 11:
        print (" ", end = "")

print()
for i in range(z*15 + 1):  
    if i == 0:
        print("          |", end = "")
    elif i%15 == 0:
        print("|", end = "")
    else:
        print ("-", end = "")
print("\n", end = "")


# Рисование графика
q = start
for i in range (count):
    print ("{:>9.3g}".format(q), end = " ")
    for j in range(z * 15 + 1):
        if j == round((z * 15 * abs(y[i] - y_min)) / (y_max + abs(y_min))):
            print ("*", end = "")
        elif intersection_with_Oy == 1 and j == round(z * 15 * abs(y_min) / (y_max + abs(y_min))):
            print("|", end = "")
        else:
            print(" ", end = "")
    print("")
    q += h

