# Типа дан файл 
# Создать функцию, которая создаёт файл состоящий из самых длинных слов каждой строки
# И потом отсортировать этот файл по длине слов
# А потом в основной проге найти кол-во используемых символов

inputFile = open('file.txt')
outputFile = open('res.txt', 'w')

punctuation = ['.', ',', ':', '!', '?', ';', '«', '»']

for line in inputFile:
    line = line.strip('\n')
    # Убираю пунктуацию
    i = 0
    while i < len(line):
        if line[i] in punctuation:
            if i == len(line) - 1:
                line = line[:i]
            else:
                line = line[:i] + line[(i+1):]
        else:
            i += 1
    # Поиск макс слова
    words = line.split()
    maxWord = ""
    for word in words:
        if len(word) > len(maxWord):
            maxWord = word
    outputFile.write(maxWord + '\n')

inputFile.close()
outputFile.close()

outputFile = open('res.txt')
words = []
for line in outputFile:
    words.append(line.strip('\n'))
outputFile.close()

# Сортировка
for i in range(1, len(words)):
    current = words[i]
    j = i - 1
    while (j >= 0 and len(current) < len(words[j])):
        words[j+1] = words[j]
        j -= 1
    words[j+1] = current

outputFile = open('res.txt', 'w')
for word in words:
    outputFile.write(word + '\n')
outputFile.close()