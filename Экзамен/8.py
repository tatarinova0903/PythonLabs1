# Сумма ряда

x = int(input("Введите x: "))
eps = float(input("Введите eps: "))

k = 1
a = b = x
sum = flag = 0
while abs(a) > eps:
    sum += a
    temp = a
    b = -1 * b * x * x / (k + 1) / (k + 2)
    a = b / (k + 2)
    if abs(a) > abs(temp):
        flag += 1
    if flag > 100:
        break 
    k += 2


if flag > 100:
    print("Ряд расходящийся при данном значении x")
else:
    print("sum =", sum)