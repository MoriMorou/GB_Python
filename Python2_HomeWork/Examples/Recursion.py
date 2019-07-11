# Рекурсивная функция

def recursion(a, b):

    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {recursion(a - 1, b)}'
    if a < b:
        return f'{a}, {recursion(a + 1, b)}'


print(recursion(20, 4))
print(recursion(3, 15))