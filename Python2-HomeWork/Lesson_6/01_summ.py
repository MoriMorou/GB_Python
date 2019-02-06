# Найти сумму и произведение цифр введённого пользователем трехзначного числа
import sum_memory


num = input('Введите трёхзначное число: ')

# решение через долнительные переменные
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summ = a + b + c
print(f'Сумма = {summ}')
print(f'Произведение = {a * b * c}')

sum_mem = sum_memory.SumMemory()
sum_mem.extend(num, a, b, c, summ)
sum_mem.print_sum()

# решение через цикл
num = str(num)
summa = 0
mult = 1
for i in num:
    summa += int(i)
    mult *= int(i)
print(f'Сумма = {summa}')
print(f'Произведение = {mult}')

sum_mem = sum_memory.SumMemory()
sum_mem.extend(num, summa, mult, i)
sum_mem.print_sum()

