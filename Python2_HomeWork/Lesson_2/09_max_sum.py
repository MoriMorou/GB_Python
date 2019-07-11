# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = int(input('Введите натуральное число. Ноль - выйти   '))
max_sum = 0
max_num = 0
while num != 0:
    spam_num = num
    spam_sum = 0
    while num > 0:
        spam_sum += num % 10
        num //= 10
    if spam_sum > max_sum:
        max_sum = spam_sum
        max_num = spam_num
    num = int(input('Введите натуральное число. Ноль - выйти   '))
print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')
