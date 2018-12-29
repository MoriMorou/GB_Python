
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
# число 3486, то надо вывести число 6843.

num = input("Input a number: ")

length = len(num)

reverse = []

for i in range(length):
    reverse.append(num[length - i - 1])

print('Reverse number is: ' + ''.join(reverse))