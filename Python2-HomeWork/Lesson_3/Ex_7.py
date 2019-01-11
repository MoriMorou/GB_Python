# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (
# оба являться минимальными), так и различаться.

import random

size = int(input("Input size fo the list "))
myList = [random.randint(-100, 100) for _ in range(size)]
print(myList)

if myList[0] > myList[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(len(myList)):
    if myList[i] < myList[min1]:
        b = min1
        min1 = i
        if myList[b] < myList[min2]:
            min2 = b
    elif myList[i] < myList[min2]:
        min2 = i

print(f'№ {min1 + 1}: {myList[min1]}')
print(f'№ {min2 + 1}: {myList[min2]}')