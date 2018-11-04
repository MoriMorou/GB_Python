
# Работа с файлами

# Флаги: r - read (можно опускать), w - write (перезапишет все содержимое файла), a - append (дописывает), wb - запись
# бинарных данных и еще rb, ab
# Если файла нет, но стоит флаг a or w, то он будет создан
# Ссылка на файл file называется файловый дескриптор

#file = open('file.txt', 'w')
#file.write('Vova, rfsha, voda\n')
#file.close()

# Библиотека os работа с файловой системой компа
import os

print(os.path.exists('123.txt'), '\n')        # проверка наличия файла (если что можно добавить путь)


# Считываем файл
file = open('file.txt')

# print(file.readline(), '\n')          # Вариант 1
for line in file:                       # Вариант 2
    print("New variant ", line)         # и можно написать line.strip() если нужно срезать табуляцию

file.seek(0)                            # Функция для перевода курсора (в скобках указывается байт) то есть если нужно
# прочитать файл с начала не закрывая его

file.close()

# Менеджер контекста with (можно использовать для контроля памяти при работе с файлами или сетивыми сокетами и т.д.)
with open('file.txt') as file:                      # мы фактически создаем ссылку на файл
    for line in file:
        print("We are printing it again ", line)    # ресурс закрывается автоматически

# Работа с переменными
a = [1, 2, 3, 4, 5]
b = a                       # переменная a and b ссылаются на один список
b.append(100)
print(a, b, '\n')           # [1, 2, 3, 4, 5, 100] [1, 2, 3, 4, 5, 100]

c = a.copy()
c.append(100)               # мы создали "поверхонстную копию" и теперь с содержит другой список и его можно менять
print(a, c, '\n')           # [1, 2, 3, 4, 5, 100] [1, 2, 3, 4, 5, 100, 100]

aa = [1, 2, 3, 4, 5, [7, 8, 9]]
d = aa.copy()
d[5].append(100)            # ВАЖНО для вложенных списков это не работает, нужен deepcopy
print(aa, d, '\n')          # [1, 2, 3, 4, 5, [7, 8, 9, 100]] [1, 2, 3, 4, 5, [7, 8, 9, 100]]


import copy

aaa = [1, 2, 3, 4, 5, [7, 8, 9]]
e = copy.deepcopy(aaa)
e[5].append(100)
print(aaa, e, '\n')         # [1, 2, 3, 4, 5, [7, 8, 9]] [1, 2, 3, 4, 5, [7, 8, 9, 100]]


# Матрица или просто двухмерный массив
# для работы с матрицами и нейросетями используется библиотека numpy

matrix = [
    [1, 2, 3],
    [3, 4, 6],
    [4, 6, 6]
]

for line in matrix:
    for num in line:
        print(num)


# AND, OR, TRUE and FALSE
print("\n")
print(1 and 0)      # оператор AND проверяет? что у нас сслево (1 это true, а 0 и пустые значения это false)
print(1 and 1)
print(0 and 0)
print(0 and 1)
print("\n")
print(1 or 0)
print(1 or 1)
print(0 or 0)
print(0 or 1)
print("\n")

# Пример
name = input('name: ')       # если не вводить имя будет гость, то есть если что пусто, то можно вывести что-то другое
print(name or 'Guest')
print(10 < 5 or '10 больше 5')     # можно пользоваться вместо if )))
print("\n")

# Тернарный оператор (сокращенная запись if and else)
age = int(input('Input age:'))
print('Welcome!' if age >= 18 else 'Good bye!')
print("\n")

# Оператор is
a = 10
b = 10
print(a is b)  # переменные указывают на один и тот же участок памяти, то есть питон кеширует

a = [1, 2]
b = [1, 2]
print(a is b)  # ВАЖНО, is работает только с неизменяемыми типами данных
print("\n")

# САХАР
# ... было...
import random

count = 10
result = []
for _ in range(count):
    result.append(random.randint(-100, 100))
print(result)

# ... было... Используем гинераторное выражение
# Как это читается? И так, читаем: для каждого значения _ из списка с 10 значениями мы применяем рандом
# или мы ставляем рандомное значение для каждого элемента в списке
result2 = [random.randint(-100, 100) for _ in range(count)]
print(result2)

result3 = [i ** 2 for i in range(count)]
print(result3)

# более сложный вариант
result4 = [i ** 2 for i in range(-10, 5) if i > 0]
print(result4)
print("\n")

# ... было... Используем гинераторные словари
result5 = {i: random.randint(-100, 100) for i in range(count)}
print(result5)


# Обработка исключений
num = [1, 2]
try:
    num[1]
except IndexError:
    print("Error, incorrect index")
except Exception as e:
    print(e.__class__)
else:
    print("You will see this message if a programme don't have errors")
finally:
    print("last information, you will see it in any time ")
print("\n")


# Регулярные выражения https://regex101.com/
# Шаблон прописыватся в []. Для одного символа одни []
# Потом указвается сколько раз может встречаться набор и все нужные символы

import re
# копируем с сайта шаблон (^ - это начало строки, $ - это конец строки
# и доп скоблки послу ^ нужны для групировки и вывода красила pettern)
pattern1 = '^(([a-zA-z!1-3_]+)@[a-z]+\.(com|ru|рф))$'
email = 'mori_Morou!13@mail.com'

print(re.search(pattern1, email))        # возвращает объект, ищет строго объект
print(re.match(pattern1, email))         # возвращает объект, ищет строго с начало строки
print(re.findall(pattern1, email))       # возвращает список

# пример поиска по группе (это те самы скобочки
search_result = re.search(pattern1, email)
if search_result:
    print("Group 1 ", search_result.group(1))
    print("Group 2 ", search_result.group(2))
    print("Group 3 ", search_result.group(3))
    print('Адрес найден')
else:
    print("Адрес не нашли")

# пример поиска номера ({9} - это колличество символов)
pattern2 = '89[0-9]{9}'
test = 'bla bla mla 89684001690 mla, bla 89684001699 mla, bla!!'
print(re.findall(pattern2, test))

