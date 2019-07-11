# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.

import random


def get_median(array):
    counter = 0
    for item in array:
        less_counter, more_counter = 0, 0
        for i in range(0, len(array)):
            if counter == i:
                continue
            if item > array[i]:
                more_counter += 1
            elif item < array[i]:
                less_counter += 1
        counter += 1
        if more_counter == less_counter:
            return item


if __name__ == '__main__':
    size = int(input("Input the number for calculation the size for the array "))
    MIN = 0
    MAX = 50
    if (size > 0):
        size = size * 2 + 1
        print(f"The size is {size}")
        array = [random.randint(MIN, MAX) for _ in range(size)]
        print(f'The array: {array}')
        print(f'The median is {get_median(array)}')
    else:
        print("Error. Check the size")