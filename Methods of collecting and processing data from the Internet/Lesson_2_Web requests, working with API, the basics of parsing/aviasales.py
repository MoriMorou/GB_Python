import requests
import pprint

flight_params = {
    'origin': 'MOW',
    'destination': 'AER',
    'one_way': 'true'
}
req = requests.get("http://min-prices.aviasales.ru/calendar_preload", params=flight_params)


data = req.json()
pprint.pprint(data)
print(data['best_prices'][0])
tickets = data['best_prices']
for ticket in tickets:
    if ticket['value'] < 3000:
        print(ticket)
