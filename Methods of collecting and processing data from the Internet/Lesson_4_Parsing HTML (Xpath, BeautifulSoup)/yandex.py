import requests
from bs4 import BeautifulSoup

# 1) С помощью BeautifulSoup спарсить новости с https://news.yandex.ru по своему региону.
# *Заголовок
# *Краткое описание
# *Ссылка на новость
# 2) * Разбить новости по категориям
# * Расположить в хронологическом порядке


def request_to_site():
    headers = {
        'accept': '*/*',
         'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    params = {}
    region = input("Input region ")
    try:
        request = requests.get(f'https://news.yandex.by/{region}/index.html', headers=headers, params=params)
        return request.text
    except requests.exceptions.ConnectionError:
        print('Please check your internet connection!')
        exit(1)


def site_title(url):
    from urllib.parse import urlparse
    parsed_uri = urlparse(url)
    return f'{parsed_uri.scheme}://{parsed_uri.netloc}'


def parse_news():
    html_doc = request_to_site()
    soup = BeautifulSoup(html_doc, 'html.parser')
    news = soup.findAll('div', {'class': 'story'})

    for index, story in enumerate(news):
        story_time = story.find('div', {'class': 'story__date'}).string.split()[-1]
        story_div = story.find('div', {'class': 'story__text'})
        if not story_div:
            story_text =''
        else:
            story_text = story_div.text
        side_hrefs = story.findAll('a')
        story_topic = side_hrefs[1].text
        story_rubric = side_hrefs[0].text
        story_rubric_href = side_hrefs[0]['href']
        story_href = side_hrefs[1]['href']
        print(index, story_time, story_rubric, story_topic, sep='-'*5)
        print(story_text, f'{site_title(story_rubric_href)}{story_href}')
        print('-'*40)


parse_news()