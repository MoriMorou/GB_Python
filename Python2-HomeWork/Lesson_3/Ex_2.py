# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

size = int(input("Input size fo the list "))
myList = [random.randint(1, 100) for _ in range(size)]
print(myList)
newList = []

for i in range(len(myList)):
    if myList[i] % 2 == 0:
        newList.append(i)
print(newList)