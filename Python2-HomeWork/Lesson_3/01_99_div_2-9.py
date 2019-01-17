# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9
# вариант 1
for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')

# вариант 2
print('вариант 2')
frequency = [0] * (END_DIV - START_DIV + 1)  # [0] * 8
for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency[j - START_DIV] += 1

for i, item in enumerate(frequency, start=START_DIV):
    print(f'Числу {i} кратно {item} чисел')
