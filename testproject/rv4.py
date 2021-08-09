from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html "
    driver.get(URL)

    # mezo, gomb, varosok az oldalon
    hianyzo_varos = driver.find_element_by_id("missingCity")
    ellenorzes_button = driver.find_element_by_id("submit")

    """cities_in_world = driver.find_element_by_id("cites").text
    list_cities = cities_in_world.split()
    print(list_cities)
    chars_to_remove = ['"', " ' "]
    subj = list_cities
    list_cities.translate(None, ''.join(chars_to_remove))
    print(list_cities)"""

    random_cities = driver.find_elements_by_xpath("//div/div/form/ul/li")
    list_cities = []
    for i in random_cities:
        city_text = i.text
        list_cities.append(i)
        print(city_text)

    # a szövegdobozban lévő városokat szerettem volna egy listába tenni, majd ezeket a listákat egyesével beírni for
    # ciklussal, függvénybe, aztán leellenőrizni, hogy milyen szöveget ír ki az app. Ha "Nem találtad el", akkor tovább
    # folytatná a kiválasztást, ha eltalálta, akkor nem.


    def talalgat():
        for city in random_cities:
            hianyzo_varos.send_keys(city.text)
            time.sleep(1)
            ellenorzes_button.click()
            time.sleep(1)
            hianyzo_varos.clear()


    talalgat()

    eredmeny = driver.find_element_by_id("result").text

    if eredmeny == "Nem találtad el.":
        talalgat()
    if eredmeny == "Eltaláltad":
        print("ok")

finally:
    pass
    # driver.close()
