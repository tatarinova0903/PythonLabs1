# Вводится строка состоящая из скобок(),[],{},нужно найти отрезок максимальной длины , где скобки расставлены правильно
# (([}[) - такого отрезка нет
# ([}{}]([])[((] - ([]), длина 4,начало-7,конец-10

str = '([{(}}]'

array = []

lengthMax = 0
startMax = 0
for j in range(len(str)):
    start = j
    length = 0
    for i in range(j, len(str)): 
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            array.insert(0, str[i])
            length += 1
        elif str[i] == ')':
            if len(array)>0 and array[0] == '(':
                array.remove('(')
                length += 1
            else:
                array.clear()
                length = 0
                break
        elif str[i] == ']':
            if len(array)>0 and array[0] == '[':
                array.remove('[')
                length += 1
            else:
                array.clear()
                length = 0
                break
        elif str[i] == '}':
            if len(array)>0 and array[0] == '{':
                array.remove('{')
                length += 1
            else:
                array.clear()
                length = 0
                break
        if len(array) == 0:
            if length > lengthMax:
                lengthMax = length
                startMax = start

if lengthMax == 0:
    print("Такого отрезка нет")
else:
    print(str[startMax:(startMax+lengthMax)])
    

