# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array, reverse=False):

    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(array):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] * sign < array[i + 1] * sign:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1
        # print(array)


SIZE = 16
LIMIT = 100
data = [random.randrange(-LIMIT, LIMIT) for _ in range(SIZE)]
print(data)
bubble_sort(data, reverse=True)
print(data)
