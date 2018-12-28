# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
# работает

import random

def check(num):
    index = 0
    while index != 10:
        index += 1
        print(f'Step {index} from 10')
        n = int(input('You number is '))
        if num == n:
            return f'You win! The number was {n}'
            break
        elif n > num:
            return 'Go down'
            continue
        else:
            print('Go up')
            continue


num = int(random.randint(0, 100))
print('Find the number for 0 to 100 ')
print(check(num))