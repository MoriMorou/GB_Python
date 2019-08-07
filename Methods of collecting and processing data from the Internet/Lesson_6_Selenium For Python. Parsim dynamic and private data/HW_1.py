from selenium import webdriver          #Основной элемент
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait   # Select - Поле множественного выбора
from selenium.webdriver.common.by import By  #используем Селениум
from selenium.webdriver.common.keys import Keys    #Клавиши клавиатуры
import pprint
from pymongo import MongoClient

link = "https://mail.ru/"
driver = webdriver.Chrome()
driver.get(link)

assert "Mail.ru: почта" in driver.title
driver.find_element_by_id("mailbox:login").send_keys('mori_morou')
Select(driver.find_element_by_id('mailbox:domain')).select_by_visible_text("@mail.ru")
driver.find_element_by_id("mailbox:password").send_keys('Volkodav!13')
driver.find_element_by_id("mailbox:submit").click()

wait = WebDriverWait(driver, 15);
wait.until(EC.title_contains("Входящие"));
assert "Входящие" in driver.title

all_items = driver.find_elements_by_xpath("//a[contains(@class,'llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal')]")

letters_info = []
for item in all_items:
#     print(item.get_attribute('innerHTML'))
    in_letter_link = item.get_attribute('href')
    one_letter_info = item.find_element_by_class_name("llc__content")
    author = one_letter_info.find_element_by_class_name("ll-crpt").get_attribute('title')
    subj = one_letter_info.find_element_by_class_name("ll-sj__normal").text
    date = item.find_element_by_class_name("llc__item_date").get_attribute('title')
    print("From: ", author, "\t\t", date, "\nSubj:", subj, "\nLink:", in_letter_link, "\n\n")
    letters_info.append({"author": author, "date": date, "subj": subj, "link": in_letter_link})

pprint.pprint(letters_info)




