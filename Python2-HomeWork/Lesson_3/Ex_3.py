# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = int(input("Input size fo the list "))
my_list = [random.randint(1, 100) for _ in range(size)]
print(my_list)

newList = sorted(my_list, key=int)
# print(newList)
min_element = newList[0]
max_element = newList[size - 1]
print(f'Min number = {min_element} and max number = {max_element}')

index_min = my_list.index(min_element)
index_max = my_list.index(max_element)
print(f'Index of min number is {index_min}, and for max is {index_max}')

my_list[index_min], my_list[index_max] = my_list[index_max], my_list[index_min]
print(my_list)

# p.s. есть и другие варианты, но я решила вспомнить сортировку

