# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
# работает


def check():
    num = str(input())
    task = int(input())
    index = 0
    for i in num:
        if int(i) == task:
            index += 1
    return index


print('Input number and task from 0 - 9 ')
print('We have', check())