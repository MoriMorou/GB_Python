import requests
from lxml import html
from pymongo import MongoClient


def request_to_site():
    headers = {
        'accept': '*/*',
        'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
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


def save_to_mongo_db():
    client = MongoClient("mongodb+srv://mori:Morou4774@cluster0-t3zhj.gcp.mongodb.net/GBdb?retryWrites=true&w=majority")
    db = client['hh']
    vacancies_db = db.vacancies
    vacancies_db.drop()

    html_page = html.fromstring(request_to_site())
    vacancies = html_page.xpath("//div[contains(@class, 'item__row_header')]")
    for vacancy in vacancies:
        try:
            salary = vacancy.xpath('.//div[contains(@class, "item__compensation")]/text()')[0]
        except IndexError:
            salary = 'no information about a salary'
        data_vacancy = {
            "title": vacancy.xpath('.//a/text()')[0],
            "link": vacancy.xpath('.//a/@href')[0],
            "salary": salary
        }
        vacancies_db.insert_one(data_vacancy)
        print('Record added')

save_to_mongo_db()