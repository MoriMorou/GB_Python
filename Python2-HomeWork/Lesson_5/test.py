med = ['', '', 0, 0]
med[0] = input('Введите ваше имя ')
med[1] = input('Введите вашу фамилию ')
med[2] = int(input('Введите ваш возраст '))
med[3] = int(input('Введите ваш вес '))
if med[3] >= 50 and med[3] <= 120:
    print(med[0], med[1], 'возраст', med[2], 'вес', med[3], 'Ты здоров')
elif med[2] <= 40 and (med[3] > 120 or med[3] < 50):
    print(med[0], med[1], 'возраст', med[2], 'вес', med[3], 'Вам нужно следить за свои здоровьем')
elif med[2] > 40 and (med[3] > 120 or med[3] < 50):
    print(med[0], med[1], 'возраст', med[2], 'вес', med[3], 'Срочно к врачу')


a = int(input('Введите число больше 0, но меньше 10 '))
while a <= 0 or a >= 10:
    print('Неверный ввод')
    a = int(input('Введите число больше 0, но меньше 10 '))
a **= 2
print('Молодец', a)

a = int(input('Введите число а '))
b = int(input('Введите число b '))
a = a + b
b = a - b
a = a - b
print('a=', a, 'b=', b)
