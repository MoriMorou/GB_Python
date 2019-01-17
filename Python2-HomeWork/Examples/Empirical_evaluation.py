# python -m timeit -n 100 -s "import Empirical_evaluation" "Empirical_evaluation.fib(10)"
import cProfile
import functools

# 1. Рекурсия
# 100 loops, best of 3: 0.0985 usec per loop    - 10

# @functools.lru_cache(maxsize=25)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# 100 loops, best of 3: 16.9 usec per loop  - 10
# 100 loops, best of 3: 198 usec per loop   - 15
# 100 loops, best of 3: 3.12 msec per loop  - 20
# 100 loops, best of 3: 34 msec per loop    - 25
# cProfile.run('fib(20)')
# 177/1    0.000    0.000    0.000    0.000 Empirical_evaluation.py:6(fib)    - 10
# 1973/1    0.000    0.000    0.000    0.000 Empirical_evaluation.py:6(fib)   - 15
# 21891/1    0.005    0.000    0.005    0.005 Empirical_evaluation.py:6(fib)  - 20


# 2. Рекурсия + словарь
def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)
# 100 loops, best of 3: 3.81 usec per loop  - 10
# 100 loops, best of 3: 8.19 usec per loop  - 25
# 100 loops, best of 3: 35.7 usec per loop  - 100
# 100 loops, best of 3: 93.2 usec per loop  - 200
# 100 loops, best of 3: 103 usec per loop   - 250
# cProfile.run('fib_dict(100)')
# 19/1    0.000    0.000    0.000    0.000 Empirical_evaluation.py:25(_fib_dict)  - 10
# 49/1    0.000    0.000    0.000    0.000 Empirical_evaluation.py:25(_fib_dict)  - 25
# 199/1    0.000    0.000    0.000    0.000 Empirical_evaluation.py:25(_fib_dict) - 100

# 3. Цикл
def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second
# 100 loops, best of 3: 0.707 usec per loop - 10
# 100 loops, best of 3: 2.72 usec per loop  - 25
# 100 loops, best of 3: 4.9 usec per loop   - 100
# 100 loops, best of 3: 12.1 usec per loop  - 100
# 100 loops, best of 3: 12.3 usec per loop  - 250
# 100 loops, best of 3: 63.2 usec per loop  - 1000
# cProfile.run('fib_loop(1000)')
# 1    0.000    0.000    0.000    0.000 Empirical_evaluation.py:43(fib_loop)

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


# test_fib(fib)
# test_fib(fib_dict)
# test_fib(fib_loop)



