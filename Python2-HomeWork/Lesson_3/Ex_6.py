# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

import random

size = int(input("Input size fo the list "))
my_list = [random.randint(1, 10) for _ in range(size)]
print(my_list)

index_min = 0
index_max = 0

for i in range(len(my_list)):
    if my_list[i] < my_list[index_min]:
        index_min = i
    elif my_list[i] > my_list[index_max]:
        index_max = i
print(f'The min index is {index_min} and the max is {index_max}')

# поменя местами индексы так как значения их не нужны
if index_min > index_max:
    index_min, index_max = index_max, index_min
print('New indexes:')
print(f'The min index is {index_min} and the max is {index_max}')
print(my_list)

summa = 0
for i in range(index_min + 1, index_max, 1):
    summa += my_list[i]
print(f'Summa is {summa}')
