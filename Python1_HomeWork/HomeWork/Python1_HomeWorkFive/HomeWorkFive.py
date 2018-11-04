# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

from Python1_HomeWorkFive import dirs as dr

dirs = ['dir_' + str(n) for n in range(1, 10)]

for cur_dir in dirs:
    dr.make_dir(cur_dir)

for cur_dir in dirs:
    dr.del_dir(cur_dir)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(dr.dir_list())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

dr.copy_file()


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def menu():
    print('Input action (1-4):')
    print('1. Go to folder')
    print('2. View the contents of the current folder')
    print('3. Delete folder')
    print('4. Create folder')
    print('To exit, type "q"')
    action = input()
    return action


def handler(action):
    if action == 'q':
        print('Exit program ...')
        print('Successful')
        return
    action_item = {
        '1': dr.change_dir,
        '2': dr.dir_list,
        '3': dr.del_dir,
        '4': dr.make_dir
        }
    item = None
    try:
        item = int(action)
        if item in range(1, 5):
            for item, key in action_item.items():
                if item == action:
                    key()
        else:
            print(f'"{action}" - incorrect command!')

    except ValueError:
        print(f'"{action}" - incorrect command!')

    answer = input('Do you want to continue??\n"y" - Yes: ')

    handler(menu()) if answer == 'y' else handler('q')

handler(menu())