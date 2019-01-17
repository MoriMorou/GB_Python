# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

size = int(input("Input size fo the list "))
my_list = [random.randint(-100, 100) for _ in range(size)]
print(my_list)

i = 0
index = -1
while i < size:
    if my_list[i] < 0 and index == -1:
        index = i
    elif my_list[i] < 0 and my_list[i] > my_list[index]:
        index = i
    i += 1

print(f'The index is {index + 1} and number is {my_list[index]}')

