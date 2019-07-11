# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# (в рамках первых трех уроков)

import sys


def sum_memory(objects):
    sum_mem = 0
    for item in objects:
        if item.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(objects[item], '__call__'):
            # убираем функции
            continue
        elif hasattr(objects[item], '__loader__'):
            # убираем модули
            continue
        else:
            """
            Тут должен быть крутой цикл из прошлого примера
            """
            sum_mem += sys.getsizeof(objects[item])
            print(f'переменная {item} класса {type(objects[item])} хранит {objects[item]} '
                  f'и занимает {sys.getsizeof(objects[item])} байт')

    return sum_mem

