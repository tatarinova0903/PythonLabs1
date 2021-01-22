
def selectionSort(array):
    for i in range(len(array)):
        minind = i
        for j in range(i, len(array)):
            if array[j] < array[minind]:
                minind = j
        array[i], array[minind] = array[minind], array[i]
    return array

def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = current
    return array

def insertionSortWithBarier(array):
    array = [0] + array
    for i in range(1, len(array)):
        array[0] = array[i]
        j = i - 1
        while array[j] > array[0]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = array[0]
    return array[1:]


def insertionSortWithBinSearch(array):
    for i in range(1, len(array)):
        current = array[i]
        start = 0
        end = i
        while start < end:
            mid = (end + start) // 2
            if current < array[mid]:
                end = mid
            else:
                start = mid + 1
        j = i - 1
        while j >= start:
            array[j+1] = array[j]
            j -= 1
        array[start] = current
    return array

def shellSort(array):
    inc = len(array) // 2
    while inc > 0:
        for i in range(len(array)):
            current = array[i]
            while i >= inc and current < array[i - inc]:
                array[i] = array[i - inc]
                i -= inc
            array[i] = current
        inc = 1 if inc == 2  else int(inc * 5.0 // 11)
    return array


def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubbleSortWithFlag(array):
    for i in range(len(array) - 1):
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break
    return array


def shakerSort(array):
    n = len(array)
    left = 0
    right = n - 1
    while left < right:
        new_right = left
        for j in range(left, right):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                new_right = j
        right = new_right

        new_left = right
        for j in range(right, left, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                new_left = j
        left = new_left

    return array

from random import randint

def quickSort(array):
    if len(array) == 0:
        return array
    randInd = randint(0, len(array) - 1)
    randElement = array[randInd]
    left = [x for x in array if x < randElement]
    rigth = [x for x in array if x > randElement]

    return quickSort(left) + [randElement] + quickSort(rigth)

print(quickSort([4, 1, 6, 3, 5, 2, 0]))