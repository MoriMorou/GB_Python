# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Input the position of letter '))
letter = ord('a') + n - 1

print('The Letter is', chr(letter))