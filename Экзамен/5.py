# Заполнение массива змейкой
# 6 5 4
# 0 1 3
# 0 0 2

N = 8

array = []
for i in range(N):
    array.append([0]*N)

x = N * (N + 1) // 2

start = 0
end = N - 1
while x != 0:
    # строка
    for i in range(start, N):
        if array[start][i] == 0:
            array[start][i] = x
            x -= 1
    # столбец
    for i in range(end+1):
        if array[i][end] == 0 and x != 0:
            array[i][end] = x
            x -= 1
    # диагональ
    i = end-1
    j = end - 1
    while i >= 0:
        if array[i][j] == 0 and x != 0:
            array[i][j] = x
            x -= 1
        i -= 1
        j -= 1
    start += 1
    end -= 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print("{:5d}".format(array[i][j]), end="")
    print()
    