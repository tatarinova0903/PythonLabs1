# text = ["Петя пошел в школу. Сегодня у него",
#         "было 3%2+4 уроков. Первым уроком", 
#         "была математика. Класс писал контрольную, за",
#         "которую Петя потом получил оценку (10+5)/5"]

# text = ["-2*6/4",
#         "4+(-2)*2",
#         "4-2*3+5",
#         "7*(2+1)+(2+3)/5",
#         "10*(20/2)",
#         "(2+2+2)^3"]

# text = ["-2 * 6 / 4",
#         "4 + (-2) * 2",
#         "4 - 2 * 3 + 5",
#         "7 * (2 + 1) + (2 + 3) / 5",
#         "10 * (20 / 2)",
#         "(2 + 2 + 2)^3",
#         "-2*6/4",
#         "4+(-2)*2",
#         "4-2*3+5",
#         "7*(2+1)+(2+3)/5",
#         "10*(20/2)",
#         "(2+2+2)^3"]


text = ["Петр 2+2*3 родился 7%4^2 июня",
        "(500+300)*2+36*2 года. Его отцом был русский царь",
        "Алексей Михайлович Романов, а матерью Наталья Нарышкина. В",
        "возрасте 2*(-10+25)%13 лет Петр потерял отца, который",
        "умер в 50-3 лет. В -9*2+1700 году после смерти царя Федора Алексеевича",
        "при дворе обострилась борьба боярских кланов."]



def sizeOfTheLongestString():
    max = 0
    for i in range(len(text)):
        if len(text[i]) > max:
            max = len(text[i])
    return max 


def printText():
    for i in range(len(text)):
        for j in range(len(text[i])):
            print(text[i][j], end="")
        print()


def onTheLeft():
    for i in range(len(text)):
            text[i] = text[i].strip()
            array = text[i].split(" ")
            text[i] = ""
            for j in range(len(array)):
                if array[j] != "":
                    if j != len(array)-1:
                        text[i] = text[i] + array[j] + " "
                    else:
                        text[i] = text[i] + array[j]

def onTheRight():
    for i in range(len(text)):
            text[i] = text[i].strip()
            array = text[i].split(" ")
            text[i] = ""
            for j in range(len(array)):
                if array[j] != "":
                    if j != len(array)-1:
                        text[i] = text[i] + array[j] + " "
                    else:
                        text[i] = text[i] + array[j]
    max = sizeOfTheLongestString()
    for i in range(len(text)):
        text[i] = text[i].strip()
        blankCount = max - len(text[i])
        text[i] = ' ' * blankCount + text[i] 

def onTheWidth():
    for i in range(len(text)):
            text[i] = text[i].strip()
    max = sizeOfTheLongestString()
    for i in range(len(text)):
        text[i].rstrip()
        blankAmungWords = len(text[i].split(" ")) - 1
        if blankAmungWords != 0:
            blankCount = (max - len(text[i])) // blankAmungWords
            stringLen = len(text[i])
            j = k = 0
            if len(text[i]) != max:
                while j < len(text[i]):
                    if text[i][j] == " ":
                        if k == (blankAmungWords - 1):
                            a = max - stringLen - blankCount*k
                            text[i] = text[i][:j] + " " * a + text[i][j:]
                            j = j + a + 2
                        else:
                            text[i] = text[i][:j] + " "*blankCount + text[i][j:] 
                            j = j + blankCount + 2
                            k += 1
                    else:
                        j += 1


def blankDelete(str):
    i = 0
    while i < len(str):
        if str[i] == " ":
            str = str[:i] + str[(i+1):]
        else:
            i += 1
    return str


def parse(string):
    while string.find('(') != -1:
        result = str(parse(string[string.find('(')+1 : string.find(')')]))
        string = string[:string.find('(')] + result + string[(string.find(')')+1):]
    indexPlus = string.find('+')
    indexMinus = string.find('-')
    if indexPlus == -1 and (indexMinus == -1 or indexMinus == 0 or not string[indexMinus - 1].isdigit()):
        indexMult = string.find('*')
        indexDiv = string.find('/')
        if indexMult == -1 and indexDiv == -1:
            indexModul = string.find('%')
            indexPow = string.find('^')
            if indexModul == -1 and indexPow == -1:
                if string == "":
                    return 0
                elif string.isdigit() or (string[0] == "-" and string[1:].isdigit):
                    return int(string)
                else:
                    return float(string)
            elif indexModul == -1 or (indexPow > indexModul and indexPow != -1):
                return parse(string[:indexPow]) ** parse(string[(indexPow+1):])
            else:    
                return parse(string[:indexModul]) % parse(string[(indexModul+1):])
        elif indexDiv == -1 or (indexMult > indexDiv and indexMult != -1):
            return parse(string[:indexMult]) * parse(string[(indexMult+1):])
        else:
            return parse(string[:indexDiv]) / parse(string[(indexDiv+1):])
    elif (indexMinus == -1 or indexMinus == 0 or not string[indexMinus - 1].isdigit()) or (indexPlus > indexMinus and indexPlus != -1):
            return parse(string[:indexPlus]) + parse(string[(indexPlus+1):])
    else:
        return parse(string[:indexMinus]) - parse(string[(indexMinus+1):])


choice = None
status = 1
while choice != 0:
    print(
        '''
        1 - Выравнивание текста по левому краю
        2 - Выравнивание текста по правому краю
        3 - Выравнивание текста по ширине
        4 - Удаление заданного слова
        5 - Замена одного слова другим во всем тексте
        6 - Вычисление арифметического выражения
        7 - Удалить самое короткое слово в самом длинном по числу слов предложении
        0 - Выход
        '''
    )
    choice = int(input('Ваш выбор: '))
    if choice == 0:
        print ('Выход')
    elif choice == 1:
        # Выравнивание текста по левому краю
        onTheLeft()
        status = 1
        printText()
    elif choice == 2:
        # Выравнивание текста по правому краю
        onTheRight()
        status = 2
        printText()
    elif choice == 3:
        # Выравнивание текста по ширине
        onTheWidth()
        status = 3
        printText()
    elif choice == 4:
        # Удаление заданного слова
        word = input("Введите слово: ")
        wordLenght = len(word)
        if wordLenght == 1:
            word = " " + word
            wordLenght += 1
        onTheLeft()
        for i in range(len(text)):
            index = text[i].find(word)
            if index == 0:
                if not (text[i][index + wordLenght] == " " or text[i][index + wordLenght] == "."):
                    index = -1
            elif index + len(word) == len(text[i]): 
                if text[i][index-1] != " ":
                    index = -1
            # elif index != -1 and (text[i][index-1] != " " or not(text[i][index+wordLenght] == " " or text[i][index+wordLenght] == "." or text[i][index+wordLenght] == ",")):
            #     index = -2

            while index != -1:
                if index + wordLenght == len(text[i]):
                    text[i] = text[i][:(index - 1)]
                elif text[i][index + wordLenght] == ".":
                    text[i] = text[i][:(index - 1)] + text[i][(index + wordLenght):]
                else:
                    text[i] = text[i][:index] + text[i][(index + wordLenght + 1):]
                index = text[i].find(word)
                if index == 0:
                    if not (text[i][index + wordLenght] == " " or text[i][index + wordLenght] == "."):
                        index = -1
                elif index + len(word) == len(text[i]): 
                    if text[i][index-1] != " ":
                        index = -1
                # elif text[i][index-1] == " " and not(text[i][index+wordLenght] == " " or text[i][index+wordLenght] == "." or text[i][index+wordLenght] == ","):
                #     index = -1
        if status == 1:
            onTheLeft()
        if status == 2:
            onTheRight()
        if status == 3:
            onTheWidth()
        printText()
    elif choice == 5:
        # Замена одного слова другим во всем тексте
        word = input("Введите слово, которое нужно заменить: ")
        wordLenght = len(word)
        newWord = input("Введите новое слово: ")
        onTheLeft()
        if wordLenght == 1:
            word = " " + word
            wordLenght += 1
        for i in range(len(text)):
            index = text[i].find(word)
            if index == 0:
                if not (text[i][index + wordLenght] == " " or text[i][index + wordLenght] == "."):
                    index = -1
            elif index + len(word) == len(text[i]): 
                if text[i][index-1] != " ":
                    index = -1
            while index != -1:
                text[i] = text[i][:index] + " " + newWord + text[i][(index + wordLenght):]
                index = text[i].find(word)
                if index == 0:
                    if not (text[i][index + wordLenght] == " " or text[i][index + wordLenght] == "."):
                        index = -1
                elif index + len(word) == len(text[i]): 
                    if text[i][index-1] != " ":
                        index = -1
        if status == 1:
            onTheLeft()
        if status == 2:
            onTheRight()
        if status == 3:
            onTheWidth()
        printText()
    elif choice == 6:
        # Вычисление арифметического выражения
        operation = ""
        for i in range(len(text)):
            j = 0
            while j < len(text[i]):
                if text[i][j].isalpha() or (text[i][j] == " " and operation == "") or (text[i][j] == " " and j != (len(text[i])-1) and (text[i][j+1].isalpha() or text[i][j+1] == " ")) or text[i][j] == "," or text[i][j] == ".":
                    if operation != "":
                        newOperation = blankDelete(operation)
                        res = parse(newOperation)
                        operationIndex = text[i].find(operation)
                        text[i] = text[i][:operationIndex] + str(res) + text[i][(operationIndex + len(operation)):]
                        j = operationIndex + len(str(res)) - 1
                        operation = ""
                elif j == (len(text[i])-1):
                    operation += text[i][j]
                    newOperation = blankDelete(operation)
                    res = parse(newOperation)
                    operationIndex = text[i].find(operation)
                    text[i] = text[i][:operationIndex] + str(res) + text[i][(operationIndex + len(operation)):]
                    j = operationIndex + len(str(res)) - 1
                    operation = ""
                else:
                    operation += text[i][j]
                j += 1
        if status == 1:
            onTheLeft()
        if status == 2:
            onTheRight()
        if status == 3:
            onTheLeft()
            onTheWidth()
        printText()
    elif choice == 7:
        # Удалить самое короткое слово в самом длинном по числу слов предложении
        # Нахождение самого длинного предложения
        maxSentence = 0
        indexRowBeginning = indexInTheRowBeginningCurrent = 0
        indexRowEnd = indexInTheRowEnd = 0
        indexRowBeginningCurrent = indexInTheRowBeginningCurrent = 0
        indexRowEndCurrent = indexInTheRowEndCurrent = 0
        count = 0
        for i in range(len(text)):
            for j in range(len(text[i])):
                if text[i][j] == '.':
                    if count > maxSentence:
                        maxSentence = count
                        indexRowBeginning = indexRowBeginningCurrent
                        indexInTheRowBeginning = indexInTheRowBeginningCurrent
                        indexRowEnd = i
                        indexInTheRowEnd = j
                    if j == (len(text[i]) - 1):
                        indexRowBeginningCurrent = i + 1
                        indexInTheRowBeginningCurrent = 0
                    else:
                        indexRowBeginningCurrent = i
                        indexInTheRowBeginningCurrent = j + 1
                    count = 0
                else:
                    count += 1

        # Нахождение самого короткого слова
        minWord = " " * 100
        word = ""
        i = indexRowBeginning
        j = indexInTheRowBeginning + 1
        indexI = indexJ = 0
        for k in range(maxSentence):
            if text[i][j].isalpha():
                word += text[i][j]
            else:
                if len(word) < len(minWord) and word != "":
                    minWord = word
                    indexI = i
                    indexJ = j
                word = ""
            if j == (len(text[i]) - 1):
                if len(word) < len(minWord) and word != "":
                    minWord = word
                    indexI = i
                    indexJ = j
                word = ""
                i += 1
                j = -1
            j += 1

        # Удаление слова
        wordLenght = len(minWord)
        indexJ -= wordLenght
        if indexJ + wordLenght == len(text[indexI]) - 1:
            text[indexI] = text[indexI][:(indexJ - 1)]
        else:
            text[indexI] = text[indexI][:indexJ] + text[indexI][(indexJ + wordLenght + 1):]
        if status == 1:
            onTheLeft()
        if status == 2:
            onTheRight()
        if status == 3:
            onTheLeft()
            onTheWidth()
        printText()
    else:
        print('Номер не найден')