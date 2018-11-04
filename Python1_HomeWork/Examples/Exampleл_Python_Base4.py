

class Car:

    def __init__(self):
        self._modules = []

    # Сложение (есть еще вычетание и т.д.)
    def __add__(self, other):
        self._modules.append(other)
        return self


car = Car()
modules = 'Booster'

# Сложение, вычитание объектов
# у объектов слево (то есть car) вызывается метод add? который отвечает за ту или иную математическую операцию
car + modules + 'helm'  # или car.__add__(modules) (одно и тоже)

print(car._modules)


# Итераторы. Задача - найти все файлы с именем log и прочетать их
import os


class LogReader:


    # Создаем список файлов, которые будут открыты
    def __init__(self):
        self.files = []

        # берем файл из кетущей директории (os.listdir())
        for file in os.listdir():
            if os.path.isdir(file):
                continue

            if file.startswith('log'):
                file_descriptor = open(file, encoding='UTF-8')
                self.files.append(file_descriptor)

        self.i = 0

    # Метод для уничтожения(закрытия) объекта
    def __del__(self):
        for file_descriptor in self.files:
            file_descriptor.close()
        print('Files closed')


    # метод для полученя итератора
    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.files):
            for line in self.files[self.i]:
                return line
            self.i += 1
        raise StopIteration       # Выбрасывает исключение


log_reader = LogReader()


# Цикл for запрашивает объект итереатор (тут это log_reader)
# Задача итератора вернуть объект у которого есть метод __next__
# Метод split удаляет переносы строк, табуляцию и т.д.
for i in log_reader:
    print(i.split())


