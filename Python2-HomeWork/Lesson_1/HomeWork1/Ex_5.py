# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Input two different letters')

p1 = ord(input('1st letter: '))
p2 = ord(input('2d letter: '))
p1 = p1 - ord('a') + 1
p2 = p2 - ord('a') + 1
result = (p2 - p1) - 1

print(f'the positions of letters are {p1} and {p2} and result is {result}')

# можно так же вытащить алфавит через модуль string

import string

a = string.ascii_lowercase
print(a)