# в матрице отсортировать столбцы по среднему арифм положительных элементов, 
# новые массивы использовать нельзя. И потом еще посчитать где больше чисел 
# кратных 5 - в нижнетреугольной или в верхнетреугольной

array = [[2, 8, -3],
         [8, -1, 5],
         [-10, 8, 2],
         [-1, -2, 2]]
m = 3
n = 4

array.append([])
for j in range(m):
    count = sum = 0
    for i in range(n):
        if array[i][j] > 0:
            count += 1
            sum += array[i][j]
    array[n].append(sum/count)

# Сортировка вставками
for i in range(1, m):
    current = array[n][i]
    currentColumn = []
    for k in range(n):
        currentColumn.append(array[k][i])
    j = i - 1
    while (j >= 0 and current < array[n][j]):
        for k in range(n):
            array[k][j+1] = array[k][j]
        j -= 1
    for k in range(n):
        array[k][j+1] = currentColumn[k]

array.remove(array[n])
for el in array:
    print(el)

countUnder = countUpper = 0
for i in range(n):
    for j in range(m):
        if i > j and array[i][j] % 5 == 0:
            countUnder += 1
        if i < j and array[i][j] % 5 == 0:
            countUpper += 1

if countUnder > countUpper:
    print("Ниже главной диагонали больше элементов, кратных 5")
elif countUnder < countUpper:
    print("Выше главной диагонали больше элементов, кратных 5")
else:
    print("Одинаково")

