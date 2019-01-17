# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (
# оба являться минимальными), так и различаться.

import random

size = int(input("Input size fo the list "))
my_list = [random.randint(-100, 100) for _ in range(size)]
print(my_list)

if my_list[0] > my_list[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(len(my_list)):
    if my_list[i] < my_list[min1]:
        b = min1
        min1 = i
        if my_list[b] < my_list[min2]:
            min2 = b
    elif my_list[i] < my_list[min2]:
        min2 = i

print(f'№ {min1 + 1}: {my_list[min1]}')
print(f'№ {min2 + 1}: {my_list[min2]}')