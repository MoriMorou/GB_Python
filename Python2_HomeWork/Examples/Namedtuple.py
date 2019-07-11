from collections import namedtuple

# Именновонный кортеж

# hero_1 = ('Vasya', 'man', 180, 84, 46, 46)
# print(hero_1[4])
#
#
# class Person:
#     pass

#     def __repr__(self, *x):
#         return f'dgrergg'

Person = namedtuple('Person', 'name, sex, height, weight, size_foot, age')
hero_2 = Person('Vasya', 'man', 180, 84, 46, 46)
print(hero_2.age)
print(type(hero_2))
print(hero_2)

print('*' * 50)
Point = namedtuple('Point', ['x', 'y', 'z'])
# Point = namedtuple('Point', ['x', 'y', 'z'], defaults=[0, 0, 0])  - нужно разобрать
p1 = Point(2, z=4, y=6)
p2 = Point(66, 23, 23)
print(p1, p2)

print(p1.x)
# p1.x = 42
p1 = p1._replace(x=42)
p3 = p1._replace(z=13)
print(p1, p2, p2, sep='\n')

print(p1._fields)
