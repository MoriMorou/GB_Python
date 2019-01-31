import sys
import gc

# рассматриваем счетчик ссылок

a = [1, 2, 3]
a.append(a)
print(a)
b = a
del a
del b
# print(sys.getrefcount(b))
print('hello')

