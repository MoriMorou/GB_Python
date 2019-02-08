
# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array):
    # ставим флаг для отражения признака отсортировки
    isSort = False
    n = 1
    while not isSort:
        isSort = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSort = False
        n += 1


if __name__ == '__main__':
    size = int(input("Input the size for the array "))
    MIN = -100
    MAX = 100

    array = [random.randint(MIN, MAX) for _ in range(size)]
    print("Old array", array)
    bubble_sort(array)
    print("Old array", array)








