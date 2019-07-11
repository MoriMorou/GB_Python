# Используя конспект, написать программу сложения и умножения
# двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого – это цифры числа.

from collections import deque


BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert(hex_num):
    deq_hex_num = deque(hex_num.upper())
    return deq_hex_num


def sum_hex(first, second):
    """
    Изменяемые объекты передаются по ссылке
    Используем копию, чтобы не ломать оригинал
    """
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    for i in range(len(first) - 1, -1, -1):
        first_num = BIN_NUMBERS[first[i]]
        second_num = BIN_NUMBERS[second[i]]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    for i in range(len(first) - 1, -1, -1):
        second_num = BIN_NUMBERS[second[i]]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first) - i - 1))
        result = sum_hex(result, spam)

    return result


if __name__ == '__main__':
    a = input('Введите первое число в hex формате (только цифры от 0 до f): ')
    b = input('Введите второе число в hex формате (только цифры от 0 до f): ')

    a = convert(a)
    b = convert(b)

    print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')
    print(f'{a} * {b} = {mult_hex(a, b)}')  # специально убрал список, чтобы показать как хранится
