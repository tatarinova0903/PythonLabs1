# Заполнение массива змейкой
# 6 5 4
# 0 1 3
# 0 0 2

N = 17

array = []
for i in range(N):
    array.append([0]*N)

x = N * (N + 1) // 2

startRow = startColumn = 0
endRow = endColumn = N - 1
while x != 0:
    # строка
    for i in range(startColumn, N):
        if array[startRow][i] == 0:
            array[startRow][i] = x
            x -= 1
    # столбец
    for i in range(startRow, endRow+1):
        if array[i][endColumn] == 0 and x != 0:
            array[i][endColumn] = x
            x -= 1
    # диагональ
    i = endRow-1
    j = endColumn - 1
    while i >= 0:
        if array[i][j] == 0 and x != 0:
            array[i][j] = x
            x -= 1
        i -= 1
        j -= 1
    startRow += 1
    startColumn += 2
    endRow -= 2
    endColumn -= 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print("{:5d}".format(array[i][j]), end="")
    print()
    