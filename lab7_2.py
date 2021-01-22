# H = [[0] * 7 for i in range(7)]
# # Ввод данных
# for i in range(7):
#     for j in range (7):
#         H[i][j] = int(input())

H = [[-4, -1, 0, 3, 8, 1, 9],
    [-2, -6, 3, 6, 1, -3 , 0],
    [-3, -5, -5, 1, 3, 0, -2],
    [-2, -4, 3, 6, 1, -3 , -4],
    [10, 2, 8, 0, -1, -2 , 9],
    [-2, -4, 2, 6, 1, -3 , 0],
    [0, 3, 3, 6, 1, 6 , 1]]

# Печать исходной матрицы
print ("Исходная матрица H:")
for i in range(7):
    for j in range(7):
        print("{:^5}".format(H[i][j]), end = " ")
    print()

for i in range(7):
    max = H[0][i]
    index_max = 0
    for j in range(7):
        if H[j][i] > max:
            max = H[j][i]
            index_max = j
    H[index_max][i], H[i][i] = H[i][i], H[index_max][i]

print("Итоговая матрица H:")
for i in range(7):
        for j in range(7):
            print("{:^5}".format(H[i][j]), end = " ")
        print()

D = []
for i in range(7):
    D.append([])
    for j in range(7):
        if i != j:
            D[i].append(H[i][j])

print("Итоговая матрица D:")
for i in range(7):
        for j in range(6):
            print("{:^5}".format(D[i][j]), end = " ")
        print()

R = []
for i in range(7):
    for j in range(6):
        if D[i][j] < 0:
            R.append(D[i][j])

print("Матрица D")
length_R = len(R)
for i in range(length_R):
    print("{:^5}".format(R[i]), end = " ")