
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