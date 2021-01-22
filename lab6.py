def is_int(str) -> bool:
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if str == '' or str == '-':
        return False
    str_in_chars = []
    for char in str:
        str_in_chars.append(char)
    length = len(str_in_chars)
    for i in range(length):
        # print(i != length - 2 or (i == length - 2 and str_in_chars[length - 1] != '0'))
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



# Поиск удвоенных согласных
def consent2(str) -> bool:
    consents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r' , 's' , 't', 'v', 'w', 'x', 'z']
    for i in consents:
        if str.find(i*2) != -1:
            return True
    return False





choice = None
while choice != 0:
    print(
        '''
        1 - Проинициализировать список первыми N элементами заданного ряда
        2 - Добавить элемент в произвольное место списка
        3 - Удалить произвольный элемент из списка
        4 - Очистить список
        5 - Найти значение K-го экстремума в списке, если он является списком чисел
        6 - Найти наиболее длинную знакочередующаяся последовательность нечётных чисел
        7 - Найти последовательность, включающую в себя наибольшее количество строк, содержащих удвоенные согласные
        0 - Выход
        '''
    )
    choice = int(input('Ваш выбор: '))
    if choice == 0:
        print ('Выход')
    elif choice == 1:
        # Проинициализировать список первыми N элементами заданного ряда
        N = input("Введите N: ")
        while not is_int(N):
            print("Вы ввели не целое число")
            N = input("Введите N: ")
        N = int(N)
        array = [0] * N
        x = input("Введите x: ")
        while not is_float(x) and not is_int(x):
            print("Вы ввели не вещественное число")
            x = input("Введите x: ")
        x = float(x)

        n = a = -1
        for i in range (N):
            n = n + 2
            a = - a / (x * x)
            array[i] = a / n

        print("Итоговый массив:", array)
    elif choice == 2:
        # Добавить элемент в произвольное место списка
        value = input("Введите значение элемента: ")
        if is_int(value):
            value = int(value)
        elif is_float(value):
            value = float(value)
        
        index = input("Введите индекс для нового элемента: ")
        while not is_int(index):
            print("Вы ввели не целое число")
            index = input("Введите индекс для нового элемента: ")
        index = int(index)
        while index > N:
            print("Индекс больше чем размер списка")
            index = int(input("Введите индекс для нового элемента: "))
            while not is_int(index):
                print("Вы ввели не целое число")
                index = input("Введите индекс для нового элемента: ")
        index = int(index)
        array.append(0)
        N += 1
        temp2 = value
        for i in range(index, N):
            temp1 = array[i]
            array[i] = temp2
            temp2 = temp1
        print("Итоговый массив:", array)
    elif choice == 3:
        # Удалить произвольный элемент из списка
        index_for_delete = input("Введите индекс элемента, который нужно удалить: ")
        while not is_int(index_for_delete):
            print("Вы ввели не целое число")
            index_for_delete = input("Введите индекс для нового элемента: ")
        index_for_delete = int(index_for_delete)
        for i in range(index_for_delete, N-1):
            array[i] = array[i+1]
        array.pop()
        N -= 1
        print("Итоговый массив:", array)
    elif choice == 4:
        # Очистить список
        array.clear()
        N = 0
        print("Итоговый массив:", array)
    elif choice == 5:
        # Найти значение K-го экстремума в списке, если он является списком чисел
        number_of_max = int(input("Введите номер для максимума: "))
        # sorted_array = array
        # sorted_array.sort()
        count = 0
        index_extr = 0
        for i in range(N-1):
            if array[i] * array[i+1] < 0:
                count += 1
                index_extr = i + 1
            if count == number_of_max:
                break
        if index_extr == 0:
            if number_of_max == 1: 
                index_extr = 0
            else:
                index_extr = N - 1
        print("{}-ый экстремум в списке:".format(number_of_max), array[index_extr])
    elif choice == 6:
        # Найти наиболее длинную знакочередующаяся последовательность нечётных чисел
        count = 1
        count_max = 0
        start = start_max = 0
        end = end_max = 0
        for i in range(N-1):
            if is_int(str(array[i])) and is_int(str(array[i+1])) and array[i]%2 == 1 and array[i]*array[i+1] < 0:
                count += 1
                end = i
            else:
                if count > count_max:
                    count_max = count
                    start_max = start
                    end_max = i
                count = 1
                start = i + 1
        print("Итоговая последовательность: ", array[start_max:end_max+1]) 
    elif choice == 7:
        # Найти последовательность, включающую в себя наибольшее количество строк, содержащих удвоенные согласные
        count = 0
        count_max = 0
        start = start_max = 0
        end = end_max = 0
        for i in range(N):
            if not is_float(str(array[i])) and not is_int(str(array[i])) and consent2(array[i]):
                count += 1
                end = i
            else:
                if count > count_max:
                    count_max = count
                    start_max = start
                    end_max = end
                count = 0
                start = i + 1
        if count > count_max:
            start_max = start
            end_max = end
        print("Итоговая последовательность: ", array[start_max:end_max + 1])
    else:
        print('Номер не найден')
