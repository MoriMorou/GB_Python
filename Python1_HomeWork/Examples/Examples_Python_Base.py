
name = "Mori moRou"

print(name.rjust(20, '*'))      # указываем длину и символ
print(name.ljust(20, '*'))      # указываем длину и символ
print(name[3])                  # i
print(name[0:3])                # Mor
print(name[:])                  # Mori moRou
print(name[0:-1])               # Mori moRo
print(name[2:4])                # ri
print(name[:4])                 # Mori
print(name[::2])                # Mr oo
print(name[::-1])               # uoRom iroM
print(len(name))                # длина строки
print(name.title())             # каждое слово с большой буквы, а другие буквы только нижний регистр
print(name.capitalize())        # только первое слово с большой буквы. остольное с маленькой
print(name.startswith('M'))     # проверка, начинается ли предложение с...., True and False
print(name.endswith("ou"))      # проверка, заканчивается ли прежложение на.... True and False
print("\n")


# index это метод для поиск куска текста
index_num = name.index("i mo")
print(index_num)                # 3
print(name[index_num:])         # iMorou
print("\n")


# split для разбивания текста по разделителю и создания списка (по умолчанию это пробел)
file_name = "Morou.html"
print(file_name.split('.'))
name, extension = file_name.split('.')
print(name, extension)
print("\n")


# Форматирование строк
my_name = 'Mori'
my_age = 30
my_money = 13.13

print('Hello! My name is %s. I am %i years old. And i have %f rubles.' % (my_name, my_age, my_money))
print('Hello! My name is {}. I am {} years old. And i have {} rubles.'.format(my_name, my_age, my_money))
print(f'Hello! My name is {my_name}. I am {my_age} years old. And i have {my_money} rubles.')
print("\n")


# Работа со списком
human = [1, 2, 'mori', 4, 4, True]   # список
print("Was ", human)
human.append('morou')                # добавление в конец списка
human.insert(1, 666)                 # добавление в начало по индексу
print("Now is ", human)
print(human.count(4))                # выводит количество повторяющихся элементов в списке
human.remove(4)                      # удаление по названию
d = human.pop(3)      # удаление с конца списка или по индексу и если нужно может вернуть значение удаленнного элемента
print("We deleted: ", d)
print("\n")


# Работа с кортежем
admins = ("Mori", "Dany", "BoyFriend")              # кортеж
for index, adm in enumerate(admins, start = 1):     # enumerate выводит и индекс и имя
    print(index, adm)
print("\n")


# Работа со словарем
address_book1 = {'name': 'Mori', 'age': 30, "address": "Moscow 41-1"}      # словать (ключ только не изменяемое)
address_book1["name"] = "Morou"                                            # меняем имя
address_book1["phone"] = 8968                                              # добавляем новый ключ и обязательно значение
print(address_book1['name'])
address_book2 = {'name': 'Dany', 'age': 12, "address": "Moscow 41-1"}
address_book2.pop("age")                                                   # удоляем пару, и ключ и значение
address_book3 = {'name': 'BoyFriend', 'age': 33, "address": "Leipzig 41-1"}
print("\n")


# Список и кортеж вмести
address_book = [address_book1, address_book2, address_book3]        # И создаем список с множеством кортежей
tuple_address_book = tuple(address_book)                            # И новый список превращаем в кортеж
print(tuple_address_book)

for key in address_book1.keys():                                    # Перебераем словарь по ключам
    print(key)

for value in address_book1.values():                                # перебор по значению
    print(value)

for key, value in address_book1.items():                            # перебор и ключам и по значению
    print(key, value)
print("\n")


# Работа с множеством
x = {1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7}                # тип set, то есть множество, хранит только уникальные значения
print(x)

a = {1, 2, 3}
b = {3, 4, 5}

print(a == b)
print(a <= b)
print(a >= b)  # a включает в себя b
print(a | b)   # объединение
print(a & b)   # точка пересечения
print(a - b)   # отнимается та часть которая пересекается
print(b - a)
print(a ^ b)   # симетрическая разность (нет точки пересечения)
print(b ^ a)
print("\n")


# Урок 3. Функции

# range() является универсальной функцией питона для создания списков (list) содержащих арифметическую прогрессию.
# Чаще всего она используется в циклах for. Функция range() может принимать от одного до трех агрументов,
# при этом аргументами должны быть целые числа (int). range(старт, стоп, шаг)
for i in range(2, 10, 2):
    print(i)
print("\n")

# Интересный эффект функции max and min for strings
print(max("aaa", "zz"))  # по асски 2zz длинее
print(max("aaa", 'zz', key=len))
print("\n")


# неопределенное колличество аргументов
def average_number (*args):
    sum = 0
    for num in args:
        sum += num
    avarage = sum / len(args)
    print("The average ", avarage)

average_number(5, 10, 15)

# если у нас есть набор чисел (лист, кортеж) и мы хотим его передать и что бы он развернулся нужно ставить *
numbers1 = [5, 10, 15]
numbers2 = {5, 10, 15}
average_number(*numbers1)
average_number(*numbers2)
print("\n")

# есть понятие аргументы по умолчанию, то есть необязательные. Важно, аргументы которые обязательные,
# должны быть первыми
def personal_name (first_name, second_name ='Guest', age = 0):
    print(first_name, second_name, age)

personal_name("Mori")
# можно менять местами, но нужно указывать название аргументов явно
personal_name("Mori", age = 20, second_name = "Morou")
print("\n")

# Если много второстепенных аргументов можно поставить **kwargs (ключ к значениям аргументы)
# То есть мы получам словарь!
def personal_name_new (**kwargs):  # можно и другое имя, а не kwargs Важны только **
    if kwargs.get('name'):
        print("Name is ", kwargs.get('name'))
    print(kwargs)

personal_name_new(name = "Mori", age = 20, phone = 4774, surname = "Morou")
print("\n")


# Создание единой функции
def personal_name_full(name, *args, surname="Cuest", **kwargs):
    print(name, surname, args, kwargs)

personal_name_full("Ivan", 13, 14, 66, 55, surname="Vodka", age=50, money=13.5)
print("\n")


# Объединение списков
dudes = ['Ivan', 'Max']
salaries = [100, 200, 300]      # 300 откинит, так как нет пары
result = zip(dudes, salaries)
print(result)                   # нужно указать преобразование объекта zip
print(list(result))             # получаем список с кортежами внутри
result = zip(dudes, salaries)   # и з-за гениратора ставим еще раз расчет результата
print(dict(result))             # получаем словарь
print("\n")

# Лямбда, упрощение записи простой функции, где есть перебор значений
# Изначальная функция
def calculation(x):
    return (x + 10) / 3

data = [-1, -2, -3, 4, 5, 6]
result = []
result2 = []
for x in data:
    result.append(calculation(x))
print(result)
print("\n")

# записываем сокращенную версию
result = map(calculation, data)          # внутри тут лямда функция
result2 = map(lambda x: (x+10)/3, data)  # в виде лямбда выражения, то есть только ОДНА строка (для одноразовых функций)
result3 = filter(lambda x: x > 0, data)  # лямбда с фильтром
print(list(result))
print(list(result2))
print(list(result3))

