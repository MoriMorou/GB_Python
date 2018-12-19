# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print('Find the sum and product of the digits of a three-digit number.')
num = int(input('Input a three-digit number '))
if num >= 0:
    n1 = int(num / 100)
    n2 = int(num / 10 % 10)
    n3 = int(num % 10)
    print(n1, n2, n3, '\n')

    a = n1 + n2 + n3
    b = n1 * n2 * n3
    print(f' The sum is {a} and product numbers {b}')

else:
    n1 = int(num / 100)
    n2 = int(num * -1 / 10 % 10)
    n3 = int(num * -1 % 10)
    print(n1, n2, n3, '\n')

    a = n1 + n2 + n3
    b = n1 * n2 * n3
    print(f' The sum is {a} and product numbers {b}')
