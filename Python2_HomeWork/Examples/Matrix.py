import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(3)]
for line in matrix:
    print(line)

sum_column = [0] * len(matrix[0])
print(sum_column)
print('*' * 50)

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item
        print(f'{item:^5}', end='')

    print(f' | {sum_line}')

for item in sum_column:
    print(f'{item:^5}', end='')
