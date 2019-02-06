class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name: {self.name} age: {self.age}'


p_1 = Person('Yaroslav', 45)
p_2 = Person('Kolya', 3)
p_3 = Person('Vasya', 100)
p_4 = Person('Lena', 72)
p_5 = Person('Petya', 8)

people = [p_1, p_2, p_3, p_4, p_5]

print(people)


# a = sorted(people)

def by_name(person):
    return person.name


b = sorted(people, key=by_name)
print(b)

from operator import attrgetter

c = sorted(people, key=attrgetter('age'))
print(c)
