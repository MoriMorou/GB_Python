import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 1000000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array.sort()    # первый этап при бинарном поиске
print(array)

find = int(input('Введите целое число для поиска: '))

# Данный алгоритм имеет асимптотику O(log n), то есть так как размер 1000? то поисп путед всегда не более 10 раз
# (2 возводим в 10ю степень = 1024)
# асимптотика — ((гр.; см. асимптота) мат. поведение функции в особых точках, чаще всего при стремлении аргумента или
# функции к бесконечности.

pos = len(array) // 2
left = 0
right = len(array) - 1
count = 1

while array[pos] != find and left <= right:
    count += 1
    if find > array[pos]:
        left = pos + 1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('Элемент отсутствует' if left > right else f'Позиция элемента {pos}') # пример тирнарного оператора
print(count)