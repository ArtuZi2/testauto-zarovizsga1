from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    URL = " https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
    driver.get(URL)

    #szamok, operandus kiolvasasa
    num1 = driver.find_element_by_id("num1")
    operandus = driver.find_element_by_id("op")
    num2 = driver.find_element_by_id("num2")

    print(num1.text)
    print(operandus.text)
    print(num2.text)

    kalkul_button = driver.find_element_by_id("submit")
    kalkul_button.click()

    result = driver.find_element_by_id("result")
    print(result.text)

    muvelet = [num1.text, operandus.text, num2.text]

    assert result.text == muvelet

finally:
    pass
    #driver.close()