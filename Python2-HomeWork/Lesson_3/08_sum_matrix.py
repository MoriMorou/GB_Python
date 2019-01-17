# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

N = 5
M = 4
matrix = []
for i in range(N):
    row = []
    summ = 0

    for j in range(M - 1):
        num = int(input(f'{i}-я строка, {j}-й элемент : '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    print(line)
