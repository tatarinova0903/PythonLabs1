# Татаринова ИУ7-14Б
# Вычисление интегралла методом парабол(Симпсона) и методом Буля

from math import sin, cos
from scipy import integrate

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
    

def is_float(str) -> bool:
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    str_in_chars = []
    for char in str:
        str_in_chars.append(char)

    is_float = True
    length = len(str_in_chars)
    ind = -1
    for i in range(length):
        if str_in_chars[i] == '.' or str_in_chars[i] == 'e':
            ind = i
    
    if ind != -1 and length != 1 and (((str_in_chars[0] == '-' and str_in_chars[1] in numbers) \
                or str_in_chars[0] in numbers or str_in_chars[0] == '.')):
        i = 1
        while i < ind:
            if str_in_chars[i] not in numbers and not(str_in_chars[i] == '.' and str_in_chars[ind] == 'e' and ind - i > 1):
                is_float = False
                break
            i += 1
        
        if ind == length - 1 and str_in_chars[ind] == 'e':
            is_float = False
        
        i = ind + 1
        while i < length:
            if str_in_chars[i] not in numbers and not(i == ind + 1 and str_in_chars[ind] == 'e' and (str_in_chars[i] == '-' or str_in_chars[i] == '+')):
                is_float = False
                break
            i += 1
    else:
        is_float = False

    return is_float




# Метод парабол(Симпсона)
def simpsonMethod(bottom, top, n, function):
    result = function(bottom) + function(top)
    h = (top - bottom) / n
    sum4 = sum2 = 0
    for i in range(1, n + 1, 2):
        sum4 += function(bottom + h * i)
        if (i + 1) != n:
            sum2 += function(bottom + h * (i + 1)) 
    result = result + 4 * sum4 + 2 * sum2 
    return result * h / 3 


# Метод Буля
def boolMethod(bottom, top, n, function):
    # result = function(bottom) * 7
    h = (top - bottom) / n
    sum7 = sum32 = sum12 = 0
    for i in range(1, int(n/4) + 1, 1):
        sum7 = sum7 + function(bottom + h * (4 * i - 4)) + function(bottom + h * (4 * i))
        sum32 = sum32 + function(bottom + h * (4 * i - 3)) + function(bottom + h * (4 * i -1)) 
        sum12 += function(bottom + h * (4 * i - 2))
    result = sum7 * 7 + sum32 * 32 + sum12 * 12
    return result * 2 * h / 45 


def function(x):
    return x*x

def antiderivative(x):
    return x**3 / 3


# Ввод данных
n1 = input("Введите n1: ")
while not is_int(n1):
    print("Вы ввели нецелое число: ")
    n1 = input("Введите n1: ")
n1 = int(n1)

n2 = input("Введите n2: ")
while not is_int(n2):
    print("Вы ввели нецелое число: ")
    n2 = input("Введите n2: ")
n2 = int(n2)

a = input("Введите нижнюю границу интегрирования: ")
while not is_float(a) and not is_int(a):
    print("Вы ввели не число")
    a = input("Введите нижнюю границу интегрирования: ")
a = float(a)

b = input("Введите верхнюю границу интегрирования: ")
while not is_float(b) and not is_int(b):
    print("Вы ввели не число")
    b = input("Введите верхнюю границу интегрирования: ")
b = float(b)
print ("{:^15}{:>7}{:<7d}{:>7}{:<7d}".format("Метод", "n1 = ", n1, "n2 = ", n2))

# Высчитываем интегралы
if n1 % 2 == 1:
    Isimpson1 = '-'
else:
    Isimpson1 = boolMethod(a, b, n1, function)
if n2 % 2 == 1:
    Isimpson2 = '-'
else:
    Isimpson2 = boolMethod(a, b, n2, function)

if n1 % 4 != 0:
    Ibool1 = '-'
else:
    Ibool1 = simpsonMethod(a, b, n1, function)
if n2 % 4 != 0:
    Ibool2 = '-'
else:
    Ibool2 = simpsonMethod(a, b, n2, function)

print("{:^15}{:^14.10}{:^14.10}".format("Метод Буля", Ibool1, Ibool2))
print("{:^15}{:^14.10}{:^14.10}".format("Метод парабол", Isimpson1, Isimpson2))

# Высчитываем точное значение интеграла
# Iexact = integrate.quad(function, a, b)[0]
Iexact = antiderivative(b) - antiderivative(a)

if abs(Ibool2 - Iexact) > abs(Isimpson2 - Iexact):
    print("Метод Буля менее точный")
    eps = float(input("Введите точность: "))
    n = n2
    I1 = boolMethod(a, b, n, function)
    I2 = boolMethod(a, b, n*2, function)
    while(abs(I1 - I2) > eps):
        n *= 2
        I1 = boolMethod(a, b, n, function)
        I2 = boolMethod(a, b, n*2, function)
    print("Значение интеграла с заданной точность:", I1, "для", n//2, "разбиений")
    absolutEstimate = abs(Iexact - I1)
    print("Абсолютная погрешность: ", absolutEstimate)
    relativeEstimate = (absolutEstimate / abs(Iexact)) * 100
    print("Относительная погрешность: ", relativeEstimate, "%")
elif abs(Ibool2 - Iexact) < abs(Isimpson2 - Iexact):
    print("Метод парабол менеее точный")
    eps = float(input("Введите точность: "))
    n = n2
    I1 = simpsonMethod(a, b, n, function)
    I2 = simpsonMethod(a, b, n*2, function)
    while(abs(I1 - I2) > eps):
        n *= 2
        I1 = simpsonMethod(a, b, n, function)
        I2 = simpsonMethod(a, b, n*2, function)
    print("Значение интеграла с заданной точность:", I1, "для", n//2, "разбиений")
    absolutEstimate = abs(Iexact - I1)
    print("Абсолютная погрешность:", absolutEstimate)
    relativeEstimate = (absolutEstimate / abs(Iexact)) * 100
    print("Относительная погрешность: {:10.8f}".format(relativeEstimate), "%", sep="")
else:
    print("Оба метода одинаково точные")

