# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

from sum_memory_2 import sum_memory


SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
for i in range(SIZE):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i
print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')

spam = array[idx_min]
array[idx_min] = array[idx_max]
array[idx_max] = spam
print(array)

print(locals())     # пример того как выглядит "локальный 'словарь'"
print('*' * 50)
print(sum_memory(locals()))


