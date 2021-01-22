# Есть файл, в нем строки содержащие латинские буквы и числа. 
# Нужно написать функцию, которая формирует файл в котором будут буквы из строк отсортированные по сумме чисел 
# в исходном файле в этой строке. А если в строке только заглавные буквы и числа, 
# то тогда оставить эти строки на тех местах, где они стояли изначально.


# abc12d2
# f3h1
# hds65tg0
# GR1
# ghwr2
# 1R890


def sumOfNumbersInString(line):
    sum = 0
    i = 0
    flag = False
    while i < len(line):
        if line[i].islower():
            flag = True
        number = 0
        while i < len(line) and line[i].isdigit():
            if number == 0:
                number = int(line[i])
            else:
                number = number * 10 + int(line[i])
            i += 1
        sum += number
        i += 1
    return (sum, flag)




count = 0

with open('file.txt') as file1:
    with open('help.txt', 'w') as file2:
        for line in file1:
            count += 1
            file2.write(line)

for i in range(count):
    file = open('help.txt')
    for j in range(i):
        file.readline()
    currentStr = file.readline()
    (currentNum, flag1) = sumOfNumbersInString(currentStr)
    file.close()

    if flag1:
        minStr = currentStr
        minNum = currentNum

        file = open('help.txt')
        for j in range(i+1):
            file.readline()
        for j in range(i+1, count):
            line = file.readline()
            (sumOfNumbers, flag2) = sumOfNumbersInString(line)
            if sumOfNumbers < minNum and flag2:
                minStr = line
                minNum = sumOfNumbers
                if line[len(line) - 1] != '\n':
                    minStr += '\n'

        file.close()
        
    
        with open('file.txt', 'w') as file1:
            with open('help.txt', 'r') as file2:
                for j in range(count):
                    line = file2.readline()
                    if line[len(line) - 1] != '\n':
                        line += '\n'
                    if line == currentStr:
                        file1.write(minStr)
                    elif line == minStr:
                        file1.write(currentStr)
                    else:
                        file1.write(line)

        with open('file.txt') as file1:
            with open('help.txt', 'w') as file2:
                for line in file1:
                    file2.write(line)