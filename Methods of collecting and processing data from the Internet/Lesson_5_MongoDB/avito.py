import pprint
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные
# объявления с avito.ru в созданную БД (xpath/BS для парсинга на выбор)
# 2) Написать функцию, которая производит поиск и выводит на экран объявления с ценой меньше введенной суммы
# *Написать функцию, которая будет добавлять в вашу базу данных только новые объявления

# Avito.ru. Пудем искать телефон HTC по названию фирмы изготовителя с выводом названия товара,
# цены, ближайшей станции метро и ссылки объявления.


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='pagination-pages clearfix')
    pages = divs.find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


# использую mongoDB cloud, так как рабочий комп
def write_mongoDB(data):
    client = MongoClient("mongodb+srv://mori:Morou4774@cluster0-t3zhj.gcp.mongodb.net/GBdb?retryWrites=true&w=majority")
    db = client['avito']
    avito_db = db.htc
    avito_db.drop()
    avito_db.insert_one(data)
    search_by_price(avito_db)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='catalog-list')
    ads = divs.find_all('div', class_='item_table')
    for ad in ads:
        try:
            div = ad.find('div', class_='description').find('h3')
            if 'htc' not in div.text.lower():
                continue
            else:
                title = div.text.strip()
        except:
            title = ''
        try:
            div = ad.find('div', class_='description').find('h3')
            url = "https://avito.ru" + div.find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''
        try:
            div = ad.find('div', class_='data')
            metro = div.find_all('p')[-1].text.strip()
        except:
            metro = ''
        data = {'title': title,
                'price': price,
                'metro': metro,
                'url': url}
        write_mongoDB(data)
        pprint.pprint(data)


def search_by_price(avito_db):
    try:
        price = int(input('\nEnter an amount to search for ads with a price less than the entered amount: '))
    except ValueError:
        print('Error. Please, inter the number, not characters')
        exit(1)
    db = avito_db.find({'price': {'$lt': price}})
    for _ in db:
        pprint.pprint(_)

def main():
    url = "https://www.avito.ru/moskva/telefony/htc?p=20&q=htc"
    base_url = "https://www.avito.ru/moskva/telefony/htc?"
    page_part = "p="
    query_par = "&q=htc"

    # total_pages = get_total_pages(get_html(url))

    # берем только три страницы (всего их 20)
    for i in range(1, 2):
        url_gen = base_url + page_part + str(i) + query_par
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
