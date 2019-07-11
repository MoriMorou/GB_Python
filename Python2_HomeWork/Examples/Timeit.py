
import time
import timeit

# start = time.time() // это плохой вариант
my_list = [i for i in range(10000)]
# delta = time.time() - start
# print(delta)

print(timeit.timeit('my_list = [i for i in range(10000)]', number=100))


# или можно обернуть всю программу в переменную

kod = """
my_list = [i for i in range(10000)]
"""
print(timeit.timeit(kod, number=100))

