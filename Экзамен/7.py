# Дан список, нужно найти самую длинную последовательность вида:
# Первый элемент равен последнему, второй равен предпоследнему и тд и записать это в новый список
# И еще сформировать список Z, который состоит из элементов изначального списка, которые повторяются более 1 раза

def search(value, array, start=0):
    for i in range(start, len(array)):
        if array[i] == value:
            return i
    return -1

def sequenceSearch(array):
    startMax = endMax = 0
    start = 0
    end = len(array) - 1
    max = 0
    for i in range(len(array)):
        start = i
        end = search(array[i], array, start+1)
        while end != -1:
            currentStart = start + 1
            currentEnd = end - 1
            while array[currentStart] == array[currentEnd]:
                if currentEnd <= currentStart:
                    if (end - start + 1) > max:
                        startMax = start
                        endMax = end
                        max = end - start + 1
                    break
                elif array[currentStart] != array[currentEnd]:
                    pass
                currentStart += 1
                currentEnd -= 1
            end = search(array[i], array, end + 1)
    res =[]
    for i in range(startMax, endMax + 1):
        res.append(array[i])
    return res
                    



def main():
    list = [4, 1, 2, 3, 3, 2, 1, 5, 1]
    res = sequenceSearch(list)
    print(res)

    Z = []
    for i in range(len(list)):
        if search(list[i], list, i+1) != -1 and search(list[i], Z) == -1:
            Z.append(list[i])
    print(Z)    


main()