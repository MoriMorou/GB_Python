
# Задание 1. Доработать приложение по поиску авиабилетов, чтобы оно возвращало билеты по названию города, а не по
# IATA коду. Пункт отправления и пункт назначения должны передаваться в качестве параметров. Сделать форматированный
# вывод, который содержит в себе пункт отправления, пункт назначения, дату вылета, цену билета (можно добавить еще
# другие параметры по желанию)

import requests
import pprint
import json


def get_best_price(place_from, place_to):
    search_place = 'Из '+place_from+' В '+place_to
    iata = json.loads(requests.get('https://www.travelpayouts.com/widgets_suggest_params?q='+search_place).text)

    if len(iata) == 0:
        return 'по вашему запросу ничего не найдено'

    iata_from = iata['origin']['iata']
    iata_to = iata['destination']['iata']

    req = requests.get('http://min-prices.aviasales.ru/calendar_preload?origin='+iata_from+'&destination='+iata_to)
    data = json.loads(req.text)

    best_price = data['best_prices'][0]
    result = {'Пункт отправления': best_price['origin'], 'Пункт назначения': best_price['destination'],
              'Дата вылета': best_price['depart_date'], 'Цена билета': best_price['value']}

    return result


best_price = get_best_price('Москва', 'париж')
pprint.pprint(best_price)

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
