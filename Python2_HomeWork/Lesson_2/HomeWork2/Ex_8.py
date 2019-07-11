# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
# работает


def check():
    num = str(input())
    digit = int(input())
    count = 0
    for i in num:
        if int(i) == digit:
            count += 1
    return count


print('Input number and task from 0 - 9 ')
print('We have', check())