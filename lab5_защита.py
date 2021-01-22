
eps = float(input("Введите eps: "))

sum = 0
a = 1
n = 1
res = a / n

while abs(res) > eps:
    sum += res
    n += 2

    a *= -1
    res = a / n
print ("Сумма ряда =", sum * 4)