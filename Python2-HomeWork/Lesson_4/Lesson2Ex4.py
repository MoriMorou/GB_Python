# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile
from datetime import datetime

def time_it(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        res_time = datetime.now() - start
        print(f'Total time is: {res_time}')
        return result
    return wrapper

@time_it
def counting_sequence_sum(n):
    item = 1
    sum_one = 0
    for _ in range(n):
        sum_one += item
        item /= -2      # item *= -0.5
    return (sum_one)

@time_it
def geometry_sum(n):
    # вариант с геометрической прогрессией
    sum_two = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return (sum_two)

if __name__ == '__main__':
    count_elements = int(input("Input the number for calculation sum: "))
    sum_one = counting_sequence_sum(count_elements)
    sum_two = geometry_sum(count_elements)
    print(f'The sum is {count_elements} elements = {sum_one} / {sum_two}')
    print("\n")


cProfile.run('counting_sequence_sum(1000000)', )
cProfile.run('geometry_sum(1000000)')

# Ответ:
# Время выполненния первого алгоритма (через цикл) (средее по трем замерам)
# Сложность: О(n) - однократное прохождение массива длины n с выполнением простой операции над каждым элементом
# Линейный рост времени выполнения в зависимости от объема входных данных

# Время выполнения второго алгоритма (через сумму геометрической прогрессии)
# Сложность: О(q^n)
# Для данного случая: O(-1/2^n)
# Время слишком мало для того, чтобы адекватно его оценивать. Модуль datetime выдает всегда нули, за редким исключением,
# которое списывается на погрешность
# p.s. также были сообщения об ошибке (результаты ниже)


# Измерения проводились тремя способами

# 1. Разница по времени
# Input the number for calculation sum: 10
# Total time is: 0:00:00.000017
# Total time is: 0:00:00.000020
# The sum is 10 elements = 0.666015625 / 0.666015625

# 2. Терминал
# python -m timeit -n 1 -s "import Lesson2Ex4" "Lesson2Ex4.counting_sequence_sum(10)"
# 1 loop, best of 5: 1.28 usec per loop  (10)
# 1 loop, best of 5: 3.7 usec per loop   (50)
# 1 loop, best of 5: 6.85 usec per loop  (100)
# 1 loop, best of 5: 73 usec per loop    (1000)
# 1 loop, best of 5: 83.5 msec per loop  (1000000)
# python -m timeit -n 1 -s "import Lesson2Ex4" "Lesson2Ex4.geometry_sum(10)"
# 1 loop, best of 5: 380 nsec per loop
# 1 loop, best of 5: 398 nsec per loop
# 1 loop, best of 5: 418 nsec per loop
# 1 loop, best of 5: 407 nsec per loop
# 1 loop, best of 5: 400 nsec per loop
# как пример ниже постоянно получала вот эту запись
# p.s. :0: UserWarning: The test results are likely unreliable. The worst time (16.8 usec) was more than four times
# slower than the best time (407 nsec).

# 3. Через cProfile
# Total time is: 0:00:00.000006
#          8 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 Lesson2Ex4.py:12(wrapper)
#         1    0.000    0.000    0.000    0.000 Lesson2Ex4.py:20(counting_sequence_sum)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method now}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Total time is: 0:00:00.000008
#          8 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 Lesson2Ex4.py:12(wrapper)
#         1    0.000    0.000    0.000    0.000 Lesson2Ex4.py:29(geometry_sum)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method now}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#          4 function calls in 0.083 seconds
#
#
# для 1000000
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.082    0.082 <string>:1(<module>)
#         1    0.082    0.082    0.082    0.082 Lesson2Ex4.py:21(counting_sequence_sum)
#         1    0.000    0.000    0.083    0.083 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson2Ex4.py:30(geometry_sum)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



