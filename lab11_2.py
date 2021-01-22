# Татаринова ИУ7-14Б
# Лабораторная работа No 11
# Имитировать работу базы данных, используя бинарный файл.
# Запись содержит 3-4 поля. Например, запись "книга" содержит поля "автор", "наименование", "год издания".
# Необходимо сделать меню:
# 1. Создание БД.
# 2. Добавление записи в БД.
# 3. Вывод всей БД.
# 4. Поиск записи по одному полю.
# 5. Поиск записи по двум полям.
# Для работы с текущей записью используется словарь.

import pickle, os.path

def printNotes(notes):
    for el in notes[0].items():
        print ("{:^25s}".format(el[0]), end="")
    print()
    for note in notes:
        for el in note.items():
            print("{:^25s}".format(el[1]), end="")
        print()

def printNote(note, i):
    if i == 0:
        for el in note.items():
            print ("{:^25s}".format(el[0]), end="")
        print()
    for el in note.items():
        print("{:^25s}".format(el[1]), end="")
    print()


choice = None
FILENAME = None
while choice != 0:
    print(
        '''
        1 - Создание БД
        2 - Добавление записи в БД
        3 - Вывод всей БД
        4 - Поиск записи по одному полю
        5 - Поиск записи по двум полям
        0 - Выход
        '''
    )
    choice = int(input('Ваш выбор: '))
    if choice == 0:
        print ('Выход')
    elif choice == 1:
        # Создание БД
        FILENAME = input("Введите название файла: ")
        if not os.path.exists(FILENAME):
            file = open(FILENAME, 'wb')
            file.close()
        N = int(input("Введите количество полей: "))
        keys = []
        for i in range(N):
            keys.append(input("Введите название поля: "))
    elif choice == 2:
        # Добавление записи в БД
        if FILENAME == None:
            FILENAME = input("Введите название файла: ")
            with open(FILENAME, "rb") as file:
                items_from_file = pickle.load(file)
                N = len(items_from_file[0].items())
                keys = []
                for key in items_from_file[0].items():
                    keys.append(key[0])
        items = []
        if os.path.getsize(FILENAME) > 0:
            with open(FILENAME, "rb") as file:
                items_from_file = pickle.load(file)
                for dictionary in items_from_file:
                    items.append(dictionary)
        file = open(FILENAME, 'wb')
        item = {}
        for i in range(N):
            item[keys[i]] = input("{}: ".format(keys[i]))
        items.append(item)
        pickle.dump(items, file)
        file.close()
    elif choice == 3:
        # Вывод всей БД
        if FILENAME == None:
            FILENAME = input("Введите название файла: ")
            with open(FILENAME, "rb") as file:
                items_from_file = pickle.load(file)
                N = len(items_from_file[0].items())
                keys = []
                for key in items_from_file[0].items():
                    keys.append(key[0])
        if os.path.getsize(FILENAME) > 0:
            with open(FILENAME, "rb") as file:
                items_from_file = pickle.load(file)
                if len(items_from_file) == 0:
                    for key in keys:
                        print ("{:^20s}".format(key), end="")
                    print()
                printNotes(items_from_file)
    elif choice == 4:
        # Поиск записи по одному полю
        if FILENAME == None:
            FILENAME = input("Введите название файла: ")
        with open(FILENAME, "rb") as file:
            items_from_file = pickle.load(file)
            i = 0
            for item in items_from_file[0].items():
                print(i+1, item[0])
                i += 1
            field = keys[int(input("Введите номер поля: "))-1]
            value = input("Введите значение: ")
            i = 0
            for item in items_from_file:
                if item[field] == value:
                    printNote(item, i)
                    i = 1
    elif choice == 5:
        # Поиск записи по двум полям
        if FILENAME == None:
            FILENAME = input("Введите название файла: ")
        with open(FILENAME, "rb") as file:
            items_from_file = pickle.load(file)
            i = 0
            for item in items_from_file[0].items():
                print(i+1, item[0])
                i += 1
            field1 = keys[int(input("Введите номер поля: "))-1]
            value1 = input("Введите значение: ")
            field2 = keys[int(input("Введите номер 2-ого поля: "))-1]
            value2 = input("Введите значение: ")
            i = 0
            for item in items_from_file:
                if item[field1] == value1 and item[field2] == value2:
                    printNote(item, i)
                    i = 1
    else:
        print('Номер не найден')