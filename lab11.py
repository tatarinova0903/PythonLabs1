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

import pickle

def printNote(note, i):
    if i == 0:
        for el in note.items():
            print ("{:^20s}".format(el[0]), end="")
        print()
    for el in note.items():
        print("{:^20s}".format(el[1]), end="")
    print()


choice = None
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
        count = 0
        N = int(input("Введите количество полей: "))
        keys = []
        for i in range(N):
            keys.append(input("Введите название поля: "))
    elif choice == 2:
        # Добавление записи в БД
        file = open('db.bin', 'rb')
        items = []
        for i in range(count):
            items.append(pickle.load(file))
        file.close()
        file = open('db.bin', 'wb')
        for el in items:
            pickle.dump(el, file)
        item = {}
        for i in range(N):
            item[keys[i]] = input("{}: ".format(keys[i]))
        pickle.dump(item, file)
        count += 1
        file.close()
    elif choice == 3:
        # Вывод всей БД
        file = open('db.bin', 'rb')
        # i = 0
        # with open('db.bin', 'rb') as file:
        #     for el in file:
        #         item = pickle.load(file)
        #         printNote(item, i)
        #         i = 1
        for i in range(count):
            item = pickle.load(file)
            printNote(item, i)
        file.close()
    elif choice == 4:
        # Поиск записи по одному полю
        file = open('db.bin', 'rb')
        for i in range(len(keys)):
            print(i+1, keys[i])
        field = keys[int(input("Введите номер поля: "))-1]
        value = input("Введите значение: ")
        for i in range(count):
            item = pickle.load(file)
            if item[field] == value:
                printNote(item, i)
        file.close()
    elif choice == 5:
        # Поиск записи по двум полям
        file = open('db.bin', 'rb')
        for i in range(len(keys)):
            print(i+1, keys[i])
        field1 = keys[int(input("Введите номер 1-ого поля: "))-1]
        value1 = input("Введите значение: ")
        field2 = keys[int(input("Введите номер 2-ого поля: "))-1]
        value2 = input("Введите значение: ")
        for i in range(count):
            item = pickle.load(file)
            if item[field1] == value1 and item[field2] == value2:
                printNote(item, i)
        file.close()
    else:
        print('Номер не найден')