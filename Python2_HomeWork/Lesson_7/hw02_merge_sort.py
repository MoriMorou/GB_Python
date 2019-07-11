# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):

    if len(array) <= 1:
        return array

    # необязательное дополненение
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


SIZE = 8
LIMIT = 50
# data = [random.uniform(0, LIMIT) for _ in range(SIZE)]
data = [round(random.uniform(0, LIMIT), 2) for _ in range(SIZE)]    # round для простоты визуальной проверки
print(data)
merge_sort(data)
print(data)
