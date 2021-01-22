# вычислить сумму ряда
# Татаринова ИУ7-14Б


x = float(input('Введите x: '))
while x < 1:
    print("Ряд расходящийся при данном значении x")
    x = float(input('Введите другой x: '))
eps = float(input('Введите eps: '))
h = int(input('Введите шаг печати: '))
max_iter = int(input('Введите максисмальное количество интераций: '))


# Печать заголовка таблицы
print ("{:^10}{:^12}{:^11}".format('N','t', 'S'))

iter = 1
sum = 0
n = 1
a = 1 / x
res = a
while abs(a) > eps and iter <= max_iter:
    # Добавление элемента к сумме
    sum += res

    # Печать текущих значений
    if iter%h == 1 or h == 1:
        print("{:^10}{:^12.3g}{:^11.4g}".format(iter, res, sum))

    # Вычисление текущего элемента
    n = n + 2
    a = - a / (x * x)
    res = a / n
    
    iter += 1

# Вывод итоговой суммы
if (iter - max_iter) == 1:
    print('за заданное число итераций вычислить сумму ряда не удалось')
else:
    print('Сумма ряда с точностью eps =', "{:7.4}".format(sum))
    print('Вычислено за {} итераций'.format(iter-1))
