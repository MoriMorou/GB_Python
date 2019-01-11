# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

size = int(input("Input size fo the list "))
myList = [random.randint(-100, 100) for _ in range(size)]
print(myList)

i = 0
index = -1
while i < size:
    if myList[i] < 0 and index == -1:
        index = i
    elif myList[i] < 0 and myList[i] > myList[index]:
        index = i
    i += 1

print(f'The index is {index + 1} and number is {myList[index]}')

