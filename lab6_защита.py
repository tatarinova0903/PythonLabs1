N = int(input("Введите N: "))
array = [0] * 100

for i in range(N):
    array[int(input("Введите число: "))] += 1



k = int(input("Введите k: "))

print("Число вхождений =", array[k])