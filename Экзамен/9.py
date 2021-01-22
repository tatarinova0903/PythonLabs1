# Написать функцию, которая формирует символьную матрицу по тексту из файла
# Удаление повторяющихся строк в матрице

def search(value, mas, start):
    for i in range(start, len(mas)):
        if mas[i] == value:
            return i
    return -1

def makeSymbolArray(filename):
    amountOfStrings = 0
    file = open(filename)
    minStr = 100000
    for line in file:
        amountOfStrings += 1
        line = line.strip('\n')
        if len(line) < minStr:
            minStr = len(line)

    res = []
    for i in range(minStr):
        res.append([0] * amountOfStrings)

    file.seek(0)
    for j in range(amountOfStrings):
        line = file.readline()
        for i in range(minStr):
            res[i][j] = line[i]

    file.close()
    return res


def deleteRepeatingStrings(mas):
    i = 0
    while i < len(mas):
        count = 1
        current = mas[i]
        for j in range(i+1, len(mas)):
            if current == mas[j]:
                count += 1
        if count > 1:
            mas.remove(current)
            if count % 2 == 0:
                index = search(current, mas, i)
                mas.remove(mas[index])
        else:
            i += 1
    return mas





array = makeSymbolArray('file.txt')

for row in array:
    print(row)

array = [[1, 2, 3],
         [4, 5, 6],
         [1, 2, 3],
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

array = deleteRepeatingStrings(array)

for row in array:
    print(row)