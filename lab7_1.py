L = int(input("Введите L: "))
M = int(input("Введите M: "))
# H = []
# # Ввод матрицы
# for i in range(L):
#     H.append([])
#     for j in range (M):
#         H[i].append(int(input()))

H = [[-4, -1, 0],
    [-2, -4, 3],
    [-3, -5, -5]]

# Поиск максимумов в столбцах
R = [0] * M
for i in range(M):
    max = H[0][i]
    for j in range (L):
        if H[j][i] > max:
            max = H[j][i]
    R[i] = max


# Замена первого отрицательного и последнего отрицательного
index_of_first_otr = index_of_last_otr = -1
flag = 1
for i in range(M):
    if R[i] < 0 and flag == 1:
        index_of_first_otr = i
        flag = 0
    if R[i] < 0:
        index_of_last_otr = i

if index_of_last_otr == -1:
    print("Отрицательных элементов нет")
else:
    R[index_of_first_otr], R[index_of_last_otr] = R[index_of_last_otr], R[index_of_first_otr]

    # Печать исходной матрицы
    print ("Исходная матрица:")
    for i in range(L):
        for j in range(M):
            print("{:^5}".format(H[i][j]), end = " ")
        print()
    # Печать итогового массива
    print("Итоговый массив")
    for i in range(M):
        print("{:^5}".format(R[i]), end = " ")  

