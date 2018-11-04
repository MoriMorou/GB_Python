import math

__author__ = "Alena Satyukova"


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Side:

    def width(self, A, B):
        # map - Позволяет применить функцию к каждому элементу последовательности, результаты функции
        # возвращает в виде итератора.
        # tuple - кортеж
        # sum - суммируем
        # round - округляем
        return round(math.sqrt(sum(tuple(map(lambda a, b: (b - a) ** 2, A, B)))), 2)

#        AB = math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)


class Triangle(Side):
    def __init__(self, A, B, C):
        self._A = A
        self._B = B
        self._C = C

    def sides(self):
        return {'AB': self.width(self._A, self._B),
                'BC': self.width(self._B, self._C),
                'CA': self.width(self._C, self._A)
                }

    def perimeter(self):
        return round(self.sides()['AB'] +
                     self.sides()['BC'] +
                     self.sides()['CA'], 2)

    def area(self):
        return round((lambda p, a, b, c:
                      math.sqrt(p * (p - a) * (p - b) * (p - c)))
                      (self.perimeter() / 2,
                       self.sides()['AB'],
                       self.sides()['BC'],
                       self.sides()['CA']), 2)

A1, A2, A3 = (2, -5), (-6, 2), (6, -2)

triangle = Triangle(A1, A2, A3)

print(f'В треугольнике со сторонами: \n Площадь: {triangle.area()} кв.см.\n Периметр: {triangle.perimeter()} см')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
