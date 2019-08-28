from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mail.ru")

# печать всего html кода страницы
print(driver.page_source)

# выполнение скрипта по заголовку страницы
assert "Mail" in driver.title

driver.close()
# cartridges = []
#
#
# for item in range(1, 10):
#     elem = driver.find_element_by_name("ctl00$MainContent$cartridgefinder$uxStep1Manufacturer")
#     all_options = elem.find_elements_by_tag_name("option")
#     brand = all_options[1].get_attribute("value")
#     all_options[1].click()
#     elem = driver.find_element_by_name("ctl00$MainContent$cartridgefinder$uxStep2machineType")
#     option = elem.find_elements_by_tag_name("option")[1]
#     family = option.get_attribute("value")
#     option.click()
#     elem = driver.find_element_by_name("ctl00$MainContent$cartridgefinder$uxStep3MachineName")
#     option = elem.find_elements_by_tag_name("option")[item]
#     printer = option.get_attribute("value")
#     option.click()
#     option = driver.find_elements_by_id("MainContent_cartridgefinder_Button1")[0]
#     option.click()
#     names = driver.find_elements_by_xpath("//a[contains(@id, 'MainContent_SearchResults_uxSearchResults_GridView_uxProductLinkTitle')]")
#     for name in names:
#         if ']' in name.text:
#             cartridge_code = name.text.split()[-3]
#         else:
#             cartridge_code = name.text.split()[-1]
#         cartridges.append((brand, family, printer, name.text, cartridge_code))
#     driver.get("https://www.officerange.com/cartridge-finder")
# driver.close()
#
# for cartridge in cartridges:
#     print(cartridge)