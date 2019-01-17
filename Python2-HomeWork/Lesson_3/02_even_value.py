# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [random.randint(MIN_ITEM, MAX_ITEM)] * SIZE
#  показать всем, что так не работает!!!
print(array)

result = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)
print(f'Индексы четных элементов: {result}')

result_new = [i for i in range(len(array)) if array[i] % 2 == 0]
print(f'Индексы четных элементов: {result_new}')
