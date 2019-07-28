import requests
import datetime

dep = input('Введите пункт отправления: ')
dest = input('Введите пункт назначения: ')
question = f'q=Из%20{dep}%20в%20{dest}'
req0 = requests.get("https://www.travelpayouts.com/widgets_suggest_params", params=question)
data0 = req0.json()
dep_iata = data0['origin']['iata']
dest_iata = data0['destination']['iata']
one_way =  input('Обратно будете возвращаться? (1 - да, 0 - нет): ')
one_way_boolean = 'true'
if one_way == '1':
    one_way_boolean = 'false'
max_value = int(input('Введите максимальну цену билета: '))
print(f'Ищем билеты из {dep_iata} в {dest_iata}...')
print(f'Поиск начат в {datetime.datetime.now()}')


flight_params = {
    'origin': dep_iata,
    'destination': dest_iata,
    'one_way': one_way_boolean
}
req = requests.get("http://min-prices.aviasales.ru/calendar_preload", params=flight_params)


data = req.json()
print(f'Поиск окончен в {datetime.datetime.now()}')
tickets = data['best_prices']

with open('aviasales_log.txt', 'w') as file:
    file.write(f'{datetime.datetime.now()}\n')
    for ticket in tickets:
        if ticket['value'] <= max_value:
            origin = ticket['origin']
            destination = ticket['destination']
            depart_date = ticket['depart_date']
            return_date = ticket['return_date']
            value = ticket['value']
        current_str = f'Пункт отправления {origin} пункт назначения {destination} дата отправления {depart_date} дата возвращения {return_date} цена {value}'
        file.write(current_str)
        file.write('\n')
        print(current_str)
file.close()