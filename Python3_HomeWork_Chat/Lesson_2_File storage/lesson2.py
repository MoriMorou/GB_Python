# Чтенние файла по строкам

file = open('links.txt')
print(file.readlines(8))
print(file.readlines(16))
print(file.readlines(64))
file.close()

print('\n')

file = open('links.txt')
print(file.read())
file.close()

print('\n')

#  Контекстные Менеджеры в Python (выводим построчно содержимое файла)
with open('links.txt') as file:
    for _ in file:
        print(_)

print('\n')

# Создание и запись файла
with open('write.txt', 'w') as file:
    file.write("First line\n")

# Дополнение данные в файл
with open('write.txt', 'a') as file:
    file.write("Second line\n")

# Рассширенный режим (чтение и изменени данных)
with open('write.txt', 'r+') as file:
    print(file.read())
    file.writelines(['New data for the file\n'])
    file.seek(0)    # перемещение коретки
    print(file.read())

# Чтение и изменение в опреденной кодировку
with open('write.txt', 'rb+') as file:
    print(file.read())
    file.writelines([b'Absolutely another test\n'])
    file.seek(0)    # перемещение коретки
    print(file.read())
print('\n')

# Запись данные по средине
import os

file_size = os.stat('write.txt').st_size
print(file_size)
file_mid = int(file_size//2)
print(file_mid)

with open('write.txt', 'rb+') as file:
    print(file.read())
    file.writelines([b' !!!!Absolutely another test (mid position)!!! \n'])
    file.seek(file_mid)    # перемещение коретки
    print(file.read())
print('\n')


#  Создание своего Контекстного Менеджера
class SampleContextManager:
    def __enter__(self, *args, **kwargs):
        return 'test'

    def __exit__(self, err, *args, **kwargs):
        pass


with SampleContextManager() as manager:
    print(manager)



