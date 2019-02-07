# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import sys

# вариант 1
num = int(input('Введите целое число: '))
print(sys.getsizeof(num))
even, odd = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print(sys.getsizeof(even))
print(sys.getsizeof(odd))
print(f"четных - {even}, нечетных - {odd}")

# вариант 2
sum_ = 0
num = int(input('Введите целое число: '))
sum_ += sys.getsizeof(num)
even, odd = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

sum_ += sys.getsizeof(even)
sum_ += sys.getsizeof(odd)
print(f"четных - {even}, нечетных - {odd}")
print(sum_)
