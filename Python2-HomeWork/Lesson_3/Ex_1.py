# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

i = 0
j = 0
myList = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            myList[j - 2] += 1

for i in range(len(myList)):
    print(f"Number {i + 2} is a multiple of {myList[i]} numbers")
