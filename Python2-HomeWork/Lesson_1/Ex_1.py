# Начало
# Вывод("Введите два числа")
# Ввод(Первое число)
# Ввод(Второе число)
# Если второечисло != 0
# то частное = первое число / второе число
# Вывод("Результат равен", частное)
# иначе Вывол ("нет решения")
# Конец

print('Input two numbers')
a = int(input('Input first number'))
b = int(input('Input second number'))

if b != 0:
    c = a/ b
    print(f'Result is {c}')
else:
    print('No solution')