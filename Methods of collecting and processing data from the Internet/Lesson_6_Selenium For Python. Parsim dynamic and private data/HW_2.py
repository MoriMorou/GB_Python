import time
from selenium import webdriver  # Основной элемент
from selenium.webdriver.common.keys import Keys  # Клавиши клавиатуры
from pymongo import MongoClient


def onlinetrade_site():
    driver = webdriver.Chrome()
    driver.get("https://www.onlinetrade.ru")
    assert "Интернет-магазин ОНЛАЙН ТРЕЙД.РУ" in driver.title
    # Ищем хиты продаж среди одинаковых заголовков. Находим ноду, содержащую заголовок и ищем ее родителя, в котором
    # уже будут и нужные товары
    headers = driver.find_elements_by_class_name("indexGoods__headers")
    for i in range(0, len(headers)):
        if headers[i].text == "Хиты продаж":
            header_hit = headers[i]
    top_hit = header_hit.find_element_by_xpath("..")

    # Все объявления среди хитов продаж
    item = top_hit.find_elements_by_class_name("indexGoods__item")

    client = MongoClient("mongodb+srv://mori:Morou4774@cluster0-t3zhj.gcp.mongodb.net/GBdb?retryWrites=true&w=majority")
    data_base = client['db_goods']  # db name
    top_hits= data_base.hits # collection name

    for i in range(0, len(item), 2):
        name = item[i].find_element_by_class_name("indexGoods__item__descriptionCover").find_element_by_tag_name(
            "a").get_attribute("title").replace("Подробнее о «", "").replace("»", "")
        link = item[i].find_element_by_class_name("indexGoods__item__descriptionCover").find_element_by_tag_name(
            "a").get_attribute("href")
        price = item[i].find_element_by_class_name("indexGoods__item__price").text
        print(name, link, price)
        top_hit = {"name": name,
                   "link": link,
                   "price": price}
        top_hits.insert_one(top_hit)

onlinetrade_site()