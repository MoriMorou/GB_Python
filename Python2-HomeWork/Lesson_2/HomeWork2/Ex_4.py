# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

length = int(input("Input n: "))
row = [1,]
summ = row[0]

for i in range(1, length):
    row.append(row[i - 1] / -2)
    summ = summ + row[i]

print(f'Sum {length} elements in line {row} \n = {summ}')