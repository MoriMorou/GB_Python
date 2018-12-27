
# Стек в python равен только 1000, нужно его увеличить через sys

import sys

sys.setrecursionlimit(2000)


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    elif m > 0 and n > 0:
        return akk(m - 1, akk(m, n - 1))


print("Akkerman function. Input 2 numbers > 0")
m = int(input())
n = int(input())
print(akk(m, n))