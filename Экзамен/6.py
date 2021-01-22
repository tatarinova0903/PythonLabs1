# Найти столбец с наибольшим количеством подряд идущих гласных и делитнуть его
# Без доп. матриц
# Все внутри функций
# Без глобальных переменных
# Транспонированная матрица == доп список => БАН
# Добавил элемент в конец => БАН

def deleteColumn(mas, n, m):
    letters = ['a', 'i', 'u', 'e', 'o', 'y']
    # Поиск нужного столбца
    indexColumn = 0
    countMax = 0
    for j in range(m):
        count = 0
        for i in range(n):
            if mas[i][j] in letters:
                count += 1
            else:
                if count > countMax:
                    countMax = count
                    indexColumn = j
                count = 0
            if i == (n - 1) and count > countMax:
                countMax = count
                indexColumn = j
    # Удаление столбца
    for i in range(n):
        mas[i].remove(mas[i][indexColumn])
    return mas


array = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['y', 'a', 'd'],
         ['i', 'e', 'a']]

res = deleteColumn(array, len(array), len(array[0]))
for i in range(len(res)):
    for j in range(len(res[0])):
        print("{:5s}".format(res[i][j]), end="")
    print()

