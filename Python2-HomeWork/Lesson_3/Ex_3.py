# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = int(input("Input size fo the list "))
myList = [random.randint(1, 100) for _ in range(size)]
print(myList)

newList = sorted(myList, key=int)
# print(newList)
min = newList[0]
max = newList[size-1]
print(f'Min number = {min} and max number = {max}')

indexMin = myList.index(min)
indexMax = myList.index(max)
print(f'Index of min number is {indexMin}, and for max is {indexMax}')

myList[indexMin], myList[indexMax] = myList[indexMax], myList[indexMin]
print(myList)

# p.s. есть и другие варианты, но я решила вспомнить сортировку

