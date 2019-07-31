import requests
from bs4 import BeautifulSoup


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
    html_doc = request_to_site()
    soup = BeautifulSoup(html_doc, 'html.parser')
    vacancies = soup.findAll('div', {'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})

    for vacancy in vacancies:
        print(vacancy.find('a').string)
        print(vacancy.find('a')['href'])
        try:
            print(vacancy.find('div', {'class': "vacancy-serp-item__compensation"}).string)
        except AttributeError:
            print("Зарплата не указана")
        print('-'*20)


parse_vacancies()
