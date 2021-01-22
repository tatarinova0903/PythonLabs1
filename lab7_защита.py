# Татаринова Дарья ИУ7-14Б

def is_int(str) -> bool:
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if str == '' or str == '-':
        return False
    str_in_chars = []
    for char in str:
        str_in_chars.append(char)
    length = len(str_in_chars)
    for i in range(length):
        if (str_in_chars[i] == '-' and i != 0) or (str_in_chars[i] != '-' and str_in_chars[i] != '.' and str_in_chars[i] not in numbers) or (str_in_chars[i] == '.' and (i != length - 2 or (i == length - 2 and str_in_chars[length - 1] != '0'))):
            return False
    return True

N = input("Введите количество строк: ")
while not is_int(N):
    print("Вы ввели не целое число: ")
    N = input("Введите количество строк: ")
N = int(N)

M = input("Введите количество столбцов: ")
while not is_int(M):
    print("Вы ввели не целое число: ")
    M = input("Введите количество строк: ")
M = int(M)

array = []
# Ввод матрицы
for i in range(N):
    array.append([])
    print("Введите элементы для {}-й строки:".format(i))
    for j in range (M):
        array[i].append(int(input()))

# Печать исходной матрицы
print("Исходная матрица: ")
for i in range(N):
    for j in range(M):
        print(array[i][j], end=" ")
    print()

# Поиск строки с максимальным количеством нулей
count_max = -1
row_index = 0
for i in range(N):
    count_null = 0
    for j in range(M):
        if array[i][j] == 0:
            count_null += 1
    if count_null > count_max:
        count_max = count_null
        row_index = i

# Перестановка строки в конец 
for k in range(N-1, row_index, -1):
    for j in range(M):
        array[row_index][j], array[k][j] = array[k][j], array[row_index][j]

# Печать итоговой матрицы
print("Итоговая матрица: ")
for i in range(N):
    for j in range(M):
        print(array[i][j], end=" ")
    print()
