from collections import defaultdict

# словарь, который встроен в питон (это реальный словарь)
a = defaultdict()
print(a)

# подсчет букв и вывод ввиде словаря
s = 'abrakadabra'
b = defaultdict(int)
for char in s:
    b[char] += 1
print(b)

# другой вариант (создаем лист)
lst = [('cat', 1), ('dog', 2), ('cat', 6), ('dog', 1), ('cat', 5), ('cat', 2), ('dog', 9)]
c = defaultdict(list)
for key, value in lst:
    c[key].append(value)
print(c)

# Вариан с лямдой
d = defaultdict(lambda: 'unknown')
d.update(rex='dog', boris='cat')
print(d)
print(d['felix'])
