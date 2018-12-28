# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


n = int(input('Input n for the len '))
line = [1.0 for i in range(0, n, 1)]
for i in line:
    if i % 2 != 0:
        line[i] = i / (- 2)
    else:
        line[i] = i / 2
print(line)

