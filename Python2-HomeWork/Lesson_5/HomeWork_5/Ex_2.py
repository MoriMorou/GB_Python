# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import copy
from collections import deque


def transform_number(number, key):
    if key == 16:
        transform_list = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    elif key == 10:
        transform_list = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    else:
        print("Error in key.")
        exit(-1)
    counter = 0
    number = copy.copy(number)
    for i in number:
        if i in transform_list:
            for j in transform_list.keys():
                if i == j:
                    number[counter] = transform_list[j]
        counter += 1
    return number


def get_sum(number_1, number_2):
    res = deque()
    num1 = transform_number(number_1, 16)
    num2 = transform_number(number_2, 16)
    i = len(num1) - 1
    j = len(num2) - 1
    memory_digit = 0
    while True:
        if i >= 0 and j >= 0:
            digit_sum = int(num1[i]) + int(num2[j]) + memory_digit
        elif i >= 0 and j < 0:
            digit_sum = int(num1[i]) + memory_digit
        elif i < 0 and j >= 0:
            digit_sum = int(num2[j]) + memory_digit
        else:
            break
        rest = digit_sum % 16
        memory_digit = digit_sum // 16
        res.appendleft(rest)
        i -= 1
        j -= 1
    return res


def get_multiply(number_1, number_2):
    res_tmp = deque()
    res = deque()
    num1 = transform_number(number_1, 16)
    num2 = transform_number(number_2, 16)
    counter = 1
    for i in num1[::-1]:
        memory_digit = 0
        for j in num2[::-1]:
            digit_sum = int(i) * int(j) + memory_digit
            rest = digit_sum % 16
            memory_digit = digit_sum // 16
            res_tmp.appendleft(rest)
        res_tmp.appendleft(memory_digit)
        if counter % 2 == 1 and counter < 3:
            res = copy.copy(res_tmp)
        else:
            res = get_sum(res_tmp, res)
        res_tmp.clear()
        for _ in range(counter):
            res_tmp.appendleft(0)
        counter += 1
    return res


if __name__ == '__main__':
    fst_number = [digit for digit in input("Input the first number in hexadecimal: ")]
    scd_number = [digit for digit in input("Input the second number in hexadecimal: ")]
    res_sum = [i for i in transform_number(get_sum(fst_number, scd_number), 10)]
    res_multiply = [i for i in transform_number(get_multiply(fst_number, scd_number), 10)]
    print(f'{fst_number} + {scd_number} = {res_sum}')
    print(f'{fst_number} + {scd_number} = {res_multiply}')