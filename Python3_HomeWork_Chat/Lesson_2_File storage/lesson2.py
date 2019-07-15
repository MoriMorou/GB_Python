# Чтенние файла по строкам

file = open('links.txt')
print(file.readlines(8))
print(file.readlines(16))
print(file.readlines(64))
file.close()

print('\n')

file = open('links.txt')
print(file.read())
file.close()

print('\n')

#  Контекстные Менеджеры в Python
with open('links.txt') as file:
    for _ in file:
        print(_)

# ЗАКОНЧИЛА НА 33 минуте