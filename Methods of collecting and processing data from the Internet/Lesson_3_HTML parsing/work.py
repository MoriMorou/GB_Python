from datetime import datetime
import requests
import json
from urllib.parse import quote

from IPython.core.display import display
from bs4 import BeautifulSoup



# ЗАДАНИЕ Необходимо собрать информацию о вакансиях на должность программиста или разработчика с сайта job.ru или hh.ru. (Можно с обоих сразу) Приложение должно анализировать несколько страниц сайта. Получившийся список должен содержать в себе:
# - Наименование вакансии,
# - Предлагаемую зарплату,
# - Ссылку на саму вакансию

headers =  {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Content-Type": 'application/json'}
url = 'https://hh.ru/search/vacancy'

result_list = []


def parse_page(page,text):
    params = dict(area='113',text=text, page=str(page),customDomain=str(1))
    request = requests.get(url, headers=headers, params=params).text
    soup = BeautifulSoup(request, 'html.parser')
    div = soup.find_all('div', attrs={"class": "vacancy-serp-item__row vacancy-serp-item__row_header"})
    for item in div:
        name = item.findChildren("a" , recursive=True)[0].text
        link = item.findChildren("a" , recursive=True)[0].attrs['href']
        salary = item.findChildren("div" , recursive=True)[2].text.replace(u'\xa0', ' ')
        result_list.append({'Наименование': name, "Зарплата": salary, "Ссылка": link})


for i in range(0,2):
    parse_page(i,'программист')
display(f'Result:')
display(result_list)

# Доработать приложение таким образом, чтобы можно было искать разработчиков на разные языки программирования (Например Python, Java, C++)

def parse_page(page, text, keywords):
    params = dict(area='113', text=text, page=str(page), customDomain=str(1))
    request = requests.get(url, headers=headers, params=params).text
    soup = BeautifulSoup(request, 'html.parser')
    div = soup.find_all('div', attrs={"class": "vacancy-serp-item__row vacancy-serp-item__row_header"})
    for item in div:
        name = item.findChildren("a", recursive=True)[0].text
        link = item.findChildren("a", recursive=True)[0].attrs['href']
        salary = item.findChildren("div", recursive=True)[2].text.replace(u'\xa0', ' ')

        if any([(lang in name.lower()) for lang in keywords]):
            result_list.append({'Наименование': name, "Зарплата": salary, "Ссылка": link})


for i in range(0, 2):
    parse_page(i, 'программист', keywords=['c++', 'python', 'java'])
display(f'Result 2:')
display(result_list)