# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за квартал для каждого.
# Программа должна определить среднюю прибыль и
# вывести наименования предприятий, чья прибыль выше среднего.
# Отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple, deque

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'\nСредняя прибыль = {average}')

# вариант 1
print(f'\nПредприятя с прибылью выше среднего:')
for comp in all_companies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработала {comp.profit}')
        # print(comp.quarters[0])   # так можно получить доступ к нужной четверти.

print(f'\nПредприятя с прибылью ниже среднего:')
for comp in all_companies:
    if comp.profit < average:
        print(f'Компания {comp.name} заработала {comp.profit}')

# вывод результат с использованием очереди - вариант 2
print('*' * 50)

sort_comp = deque([None])
for comp in all_companies:
    if comp.profit > average:
        sort_comp.append(comp)
    elif comp.profit < average:
        sort_comp.appendleft(comp)

text = 'меньше'
for comp in sort_comp:
    if comp is None:
        text = 'больше'
    else:
        print(f'Компания {comp.name} заработала {text}, чем средняя прибыль - {comp.profit}')
