
N = int(input("Введите количество строк: "))
M = int(input("Введите количтсво столбцов: "))

array = []
for i in range(N):
    array.append([])
    print("Введите элементы для {}-й строки".format(i))
    for j in range(M):
        array[i].append(int(input()))

# Печать исходной матрицы
print("Исходная матрица: ")
for i in range(N):
    for j in range(M):
        print(array[i][j], end=" ")
    print()


# Поиск столбца с макимальной суммой элементов
max_sum = 0
index = 0
for j in range(M):
    sum = 0
    for i in range(N):
        sum += array[i][j]
    if sum > max_sum:
        max_sum = sum
        index = j

# Вставка столбца
for i in range(N):
    for j in range(M):
        if j == index:
            array[i].insert(j+1, array[i][j]*2)

# Печать итоговой матрицы
print("Итоговая матрица: ")
for i in range(N):
    for j in range(M+1):
        print(array[i][j], end=" ")
    print()