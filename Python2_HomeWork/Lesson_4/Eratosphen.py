
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа
# сохранить в виде комментариев в файле с кодом.

import cProfile
from datetime import datetime

def eratosphen_primes(limit):
    limitn = limit + 1
    not_prime = [False] * limitn

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i * 2, limitn, i):
            not_prime[f] = True
        yield i


def primes(n = 1):
    while True:
        if isprime(n):
            yield n
        n += 1


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def find_prime_number(index_number, func):
    counter = 1
    start_time = datetime.now()
    for n in func:
        if counter == index_number:
            print("Total time is: ", datetime.now() - start_time)
            return n
        counter += 1
    return -1

if __name__ == '__main__':
    print(find_prime_number(5000, primes()))
    print(find_prime_number(5000, eratosphen_primes(49000)))

cProfile.run("find_prime_number(5000, primes())")
cProfile.run("find_prime_number(5000, eratosphen_primes(49000))")

# ОТВЕТ:
# 1. способ для 5000
# Время работы алгоритмов (среднее по трем замерам)
#           Не Решето       Решето      Быстрее (раз)
# 1000      0,617642с       0,008025c       77
# 2000      2,687465с       0,017547c       153
# 3000      6,260159c       0,027072c       231
# 4000      12,417258c      0,036598c       339
# 5000      21,989743с      0,049599с       443
#
# 2. второй способ
#
#          53619 function calls in 9.060 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    9.060    9.060 <string>:1(<module>)
#      5001    0.011    0.000    9.058    0.002 Eratosphen.py:23(primes)
#     48611    9.047    0.000    9.047    0.000 Eratosphen.py:30(isprime)
#         1    0.002    0.002    9.060    9.060 Eratosphen.py:39(find_prime_number)
#         1    0.000    0.000    9.060    9.060 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method now}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Total time is:  0:00:00.011506
#          5008 function calls in 0.012 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#      5001    0.011    0.000    0.011    0.000 Eratosphen.py:11(eratosphen_primes)
#         1    0.001    0.001    0.012    0.012 Eratosphen.py:39(find_prime_number)
#         1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method now}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Из приведенной таблицы видно, что в результате практического эксперимента были получены следующие данные.
# Анализируя их, можно сделать вывод, что алгоритм решета для поиска простых чисел работает в разы быстрее алгоритма
# 'не решето' силы. Более того, можно заметить, что при увеличении объема данных, отношение времени работы метода грубой силы
# к времени работы решета стремительно растет. Таким образом, можно сделать вывод, что на значительных объемах данных
# алгоритм решета работает гораздо быстрее.
#
# Алгоритм "решета":
# O(n * log(log n)) - информация из открытых источников. Обоснование лежит на википедии, не представляет собой
# ничего сложного (коопировать сюда не стала). (Строго математическое). Практические результаты подтверждают
# теорию (при построение графика получается логарифмическая кривая)
# Существует реализация снижающая сложность до O(sqrt(n)) через корни (не учитывая половины перебора
#
# Алгоритм "не решето":
# O(n) - перебор всех элементов по порядку до поиска нужного и проверка каждого
# O(n) - для каждого элемента перебираем все делители от 2 до n
# Суммарная теоретическая сложность: O(n^2)
# Результаты сильно колеблются
