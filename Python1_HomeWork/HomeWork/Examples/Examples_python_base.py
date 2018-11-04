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


index_num = name.index("i mo")  # index это метод для поиск куска текста
print(index_num)                # 3
print(name[index_num:])         # iMorou

file_name = "Morou.html"
print(file_name.split('.'))     # split для разбивания текста по разделителю и создания списка (по умолчанию это пробел)
name, extension = file_name.split('.')
print(name, extension)

# Форматирование строк
my_name = 'Mori'
my_age = 30
my_money = 13.13

print('Hello! My name is %s. I am %i years old. And i have %f rubles.' % (my_name, my_age, my_money))
print('Hello! My name is {}. I am {} years old. And i have {} rubles.'.format(my_name, my_age, my_money))
print(f'Hello! My name is {my_name}. I am {my_age} years old. And i have {my_money} rubles.')

human = [1, 2, 'mori', 4, 4, True]   # список
print("Was ", human)
human.append('morou')                # добавление в конец списка
human.insert(1, 666)                 # добавление в начало по индексу
print("Now is ", human)
print(human.count(4))                # выводит количество повторяющихся элементов в списке
human.remove(4)                      # удаление по названию
d = human.pop(3)      # удаление с конца списка или по индексу и если нужно может вернуть значение удаленнного элемента
print("We deleted: ", d)

admins = ("Mori", "Dany", "BoyFriend")              # кортеж
for index, adm in enumerate(admins, start = 1):     # enumerate выводит и индекс и имя
    print(index, adm)

address_book1 = {'name': 'Mori', 'age': 30, "address": "Moscow 41-1"}      # словать (ключ только не изменяемое)
address_book1["name"] = "Morou"                                            # меняем имя
address_book1["phone"] = 8968                                              # добавляем новый ключ и обязательно значение
print(address_book1['name'])
address_book2 = {'name': 'Dany', 'age': 12, "address": "Moscow 41-1"}
address_book2.pop("age")                                                   # удоляем пару, и ключ и значение
address_book3 = {'name': 'BoyFriend', 'age': 33, "address": "Leipzig 41-1"}

address_book = [address_book1, address_book2, address_book3]        # И создаем список с множеством кортежей
tuple_address_book = tuple(address_book)                            # И новый список превращаем в кортеж
print(tuple_address_book)

for key in address_book1.keys():                                    # Перебераем словарь по ключам
    print(key)

for value in address_book1.values():                                # перебор по значению
    print(value)

for key, value in address_book1.items():                            # перебор и ключам и по значению
    print(key, value)


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





