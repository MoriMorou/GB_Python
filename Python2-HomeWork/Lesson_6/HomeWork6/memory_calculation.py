
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.


import sys

# hasattr() - Возвращает флаг, указывающий на то, содержит ли объект указанный атрибут. Возвращает True, если атрибут
# существует, иначе — False.
# getattr() - Возвращает значение атрибута объекта.
# https://habr.com/ru/company/mailru/blog/336156/
# https://habr.com/ru/post/193890/


def show_sizeof(x, memory_list, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    memory_list.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_sizeof(key, memory_list, level + 1)
                show_sizeof(value, memory_list, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_sizeof(item, memory_list, level + 1)


def memory_size(user_objects):
    sum_mem = 0
    for obj in user_objects:
        mem_list = []
        if obj.startswith('__'):
            continue
        elif hasattr(user_objects[obj], '__call__'):
            continue
        elif hasattr(user_objects[obj], '__loader__'):
            continue
        else:
            show_sizeof(user_objects[obj], mem_list)
            for item in mem_list:
                sum_mem += item
    return f'The total sum of memory is: {sum_mem} byte'
