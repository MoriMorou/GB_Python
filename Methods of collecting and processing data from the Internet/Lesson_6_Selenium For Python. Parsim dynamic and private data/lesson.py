from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Ввод данных

driver = webdriver.Chrome()

driver.get('https://geekbrains.ru/login')
assert "GeekBrains" in driver.title

# Заполняеи поля ввода по id
elem = driver.find_element_by_id("user_email")
elem.send_keys('example-for-geekbrains@mail.ru')
elem = driver.find_element_by_id("user_password")
elem.send_keys('password-example')
elem.send_keys(Keys.RETURN)   #эмитация нажатия кнопки enter

driver.close()