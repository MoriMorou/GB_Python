from collections import Counter

# разные варианты создания множества
a = Counter()
b = Counter('adcadauuuuu')
c = Counter({'cat': 15, 'dog': 5})
d = Counter(cats=2, dogs=4)
print(a, b, c, d, sep='\n')

print("Прверяем наличие {z}", b['z'])
print("Прверяем наличие {a}", b['a'])

b['z'] = 4
print('Мы добавили {z} и получили\n', b)

# Он воращает лист с картежами (tuple)
print("Самый часто встречающийся объект", b.most_common(3),'\n')

# если итератор (ссылку на объект) обвернуть в список то мы получим список (см ниже)
print('Итератор (ссылка)' , b.elements())
print('Итератор (ссылку) обвернули в list ', list(b.elements()), '\n')

e = Counter(a=1, b=-2, c=3)
f = Counter(a=3, b=-1, c=-4)
print(list(e.elements()))
print(e, f, sep='\n')

print("Сумма", e + f)
print("Разница", e - f)
print("Пересечение", e & f) # по меньше элементу
print("Или (дизьюнция)", e | f) # по макс положительному элементу
