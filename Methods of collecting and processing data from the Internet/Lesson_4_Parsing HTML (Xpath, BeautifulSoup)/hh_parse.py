import requests
from lxml import html


def request_to_site():
    headers = {
        'accept': '*/*',
         'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    params = {
        'text': 'программист'
    }
    try:
        request = requests.get('https://hh.ru/search/vacancy', headers=headers, params=params)
        return request.text
    except requests.exceptions.ConnectionError:
        print('Please check your internet connection!')
        exit(1)


def parse_vacancies():
    html_page = html.fromstring(request_to_site())
    vacancies = html_page.xpath("//div[contains(@class, 'item__row_header')]")[:5]
    for vacancy in vacancies:
        print(vacancy.xpath('.//a/text()')[0])
        print(vacancy.xpath('.//a/@href')[0])
        try:
            print(vacancy.xpath('.//div[contains(@class, "item__compensation")]/text()')[0])
        except IndexError:
            print('Зарплата не указана')
        print('-'*25)


parse_vacancies()
