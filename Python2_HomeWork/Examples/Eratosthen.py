# Решето Эратосфена – алгоритм определения простых чисел
# 0 и 1 простыми числами не является и решето начинается с 2. С двух мы начинаем определять простые и состовные числа

n = int(input('До какого числа просеивать решето: '))

sieve = [i for i in range(n + 1)]
print(sieve)
sieve[1] = 0

for i in range(2, n + 1):
    if sieve[i] != 0:
        j = i + i
        while j < n + 1:
            sieve[j] = 0
            j += i
print(sieve)
result = [i for i in sieve if i != 0]
print(result)

# range бывает трех видов
# range(stop)
# range(start, stop)
# range(start, stop, step)

