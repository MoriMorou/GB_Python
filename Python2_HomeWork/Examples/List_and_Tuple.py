# list - список

a = [1, 2, 3]
b = a
#  тут создается новый объект
a = a + [4, 5]
print(a, b, sep='\n')

a = [1, 2, 3]
b = a
# тут не создается новый объект, а изменяется старый или это равнозначно a.extend[4, 5]
a += [4, 5]
print(a, b, sep='\n')


# tuple - кортеж

tup = ('one')
for item in tup:
    print(item)
print(type(tup))

tup = ('one',)  # ВНИМАНИЕ на запятую
for item in tup:
    print(item)
print(type(tup))


tup = ('one', 'two')
for item in tup:
    print(item)
print(type(tup))