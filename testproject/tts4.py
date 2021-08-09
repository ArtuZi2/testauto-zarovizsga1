from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
    driver.get(URL)

    # Száz gombnyomás
    penzfeldobas_gomb = driver.find_element_by_id("submit")
    for i in range(100):
        penzfeldobas_gomb.click()

    time.sleep(2)
    # eredményekből kivettem a fejet, majd listába tettem
    results = driver.find_elements_by_xpath("//div/div/ul/li")
    fej_result = []
    for i in results:
        if i.text == "fej":
            fej_result.append(i.text)
    elvart_min_fej = 30

    # ellenőriztem, hogy az elvártnál több fej van-e a listában
    assert elvart_min_fej < len(fej_result)


finally:
    pass
    driver.close()
