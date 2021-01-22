# Татаринова Дарья И7-14Б

N = int(input("Введите N: "))

array = [[0] * N for i in range(N)]

k = 1
for i in range(N):
    str = input()
    str_in_chars = []
    for char in str:
        str_in_chars.append(char)
    for j in range(k):
        array[i][j] = str_in_chars[j]
    if i < N//2:
        k += 1
    else:
        k -= 1

# Симметрия относительно побочной диагонали
for i in range(N):
    for j in range(N):
        if i + j < N - 1:
            array[i + abs(N-1 - (i+j))][j + abs(N-1 - (i+j))] = array[i][j]

# Симметрия относительно главной диагонали
for i in range(N):
    for j in range(N):
        if i < j:
            array[i][j] = array[j][i]

print("После разворота листа: ")
for i in range(N):
    for j in range(N):
        print(array[i][j], end=" ")
    print()


# Сортировка
j_max= -1
for k in range(N-1, -1, -1):
    count_max = -1
    for j in range(k+1):
        count = 0
        for i in range(N):
            if array[i][j] == ".":
                count += 1
        if count > count_max:
            count_max = count
            j_max = j
    for i in range(N):
        array[i][k], array[i][j_max] = array[i][j_max], array[i][k]


print("Матрица после сортировки:")
for i in range(N):
    for j in range(N):
        print(array[i][j], end=" ")
    print()