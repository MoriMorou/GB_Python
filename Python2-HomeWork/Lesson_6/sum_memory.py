# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# (в рамках первых трех уроков)

import sys


class SumMemory:

    def __init__(self):
        """
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        """
        self._sum_memory = 0
        self._types = {}

    def extend(self, *args):
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        eggs = str(obj.__class__)
        self._sum_memory += spam
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1] * 2
            self._types[eggs][1] = spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def print_sum(self):
        print(f'Переменные заняли в сумме {self._sum_memory} байт')
        for key, value in self._types.items():
            print(f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт')

