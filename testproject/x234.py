from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
    driver.get(URL)

    # tesztadatok
    a = [99, "kiskutya", " "]
    b = [12, 12, " "]

    # TC01: helyes kitöltés
    driver.find_element_by_id("a").send_keys(a[0])
    driver.find_element_by_id("b").send_keys(b[0])
    calc_button = driver.find_element_by_id("submit")
    calc_button.click()
    print(driver.find_element_by_id("result").text)
    result = driver.find_element_by_id("result").text
    data_expected = '222'
    print(data_expected)

    assert data_expected == result
    time.sleep(1)

    # TC02: nem számokkal
    driver.find_element_by_id("a").clear()
    driver.find_element_by_id("b").clear()

    driver.find_element_by_id("a").send_keys(a[1])
    driver.find_element_by_id("b").send_keys(b[1])
    calc_button.click()

    data_expected2 = 'NaN'

    print(data_expected2)
    result2 = driver.find_element_by_id("result").text

    assert result2 == data_expected2

    # Üres kitöltés
    driver.find_element_by_id("a").clear()
    driver.find_element_by_id("b").clear()

    driver.find_element_by_id("a").send_keys(a[2])
    driver.find_element_by_id("b").send_keys(b[2])
    calc_button.click()

    data_expected3 = 'NaN'
    result3 = driver.find_element_by_id("result").text
    assert result3 == data_expected3

finally:
    driver.close()
