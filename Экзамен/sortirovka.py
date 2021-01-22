
count = 0

# Перепишем все в файл-помощник
with open('file.txt') as file1:
    with open('help.txt', 'w') as file2:
        for line in file1:
            count += 1
            file2.write(line)

for i in range(count):
    # Запоминаем текущее значение (первый элемент в неотсортированной части)
    file = open('help.txt')
    for j in range(i):
        file.readline()
    current = file.readline()
    file.close()

    # Пусть пока что минимум - это первое значение в неотсортированной части
    min = current
    minind = i

    # Поиск минимума
    file = open('help.txt')
    for j in range(i+1):
        file.readline()
    for j in range(i+1, count):
        line = file.readline()
        if int(line) < int(min):
            min = line
            if line[len(line) - 1] != '\n':
                min += '\n'

    file.close()
        
    # Меняем местами минимум и первый элемент неотсортированной части
    with open('file.txt', 'w') as file1:
        with open('help.txt', 'r') as file2:
            for j in range(count):
                line = file2.readline()
                if line[len(line) - 1] != '\n':
                    line += '\n'
                if line == current:
                    file1.write(min)
                elif line == min:
                    file1.write(current)
                else:
                    file1.write(line)

    # Обновляем файл-помощник
    with open('file.txt') as file1:
        with open('help.txt', 'w') as file2:
            for line in file1:
                file2.write(line)