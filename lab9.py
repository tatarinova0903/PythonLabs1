# Определение кода буквы
def letterCode(letter) -> int:
    return ord(letter) - 97


choice = None
str = ""
while choice != 0:
    print(
        '''
        1 - Ввод строки
        2 - Настройка шифрующего алгоритма
        3 - Шифрование строки, используя шифр Виженера
        4 - Расшифровывание строки
        0 - Выход
        '''
    )
    choice = int(input('Ваш выбор: '))
    if choice == 0:
        print ('Выход')
    elif choice == 1:
        # Ввод строки
        str = input("Введите строку: ")
        str.lower
        strLen = len(str)
        print("Вы ввели:", str)
    elif choice == 2:
        # Настройка шифрующего алгоритма
        key = input("Введите ключ для шифрования: ")
        key.lower
        keyLen = len(key)
        resultKey = ""
        j = 0
        for i in range(strLen):
            if str[i] == " ":
                resultKey += " "
            else:
                resultKey += key[j % keyLen]
                j += 1
        print(resultKey)
    elif choice == 3:
        # Шифрование строки, используя шифр Виженера
        cipher = ""
        for i in range(strLen):
            if str[i] == " ":
                cipher += " "
            else:
                code = letterCode(str[i]) + letterCode(resultKey[i])
                if code > 26:
                    code -= 26
                cipher += chr(code + 97)
        print("Строка после шифрования:", cipher)
    elif choice == 4:
        # Расшифровка строки
        str = ""
        for i in range(strLen):
            if resultKey[i] == " ":
                str += " "
            else:
                code = letterCode(cipher[i]) - letterCode(resultKey[i])
                if code < 0:
                    code += 26
                str += chr(code + 97)
        print("Строка после расшифровки:", str)
    else:
        print('Номер не найден')