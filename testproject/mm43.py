from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"
    driver.get(URL)

    # TC1 helyes kitöltés:
    email = driver.find_element_by_id("email")
    email.send_keys("teszt@elek.hu")
    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

    #assert (driver.find_element_by_class_name("validation-error")).is_displayed()

    # TC02 helytelen kitöltés:
    email.clear()
    email.send_keys("teszt@")
    submit_button.click()
    vallidation_error = driver.find_element_by_class_name("validation-error").text
    assert_message = "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

    assert assert_message is not None
    assert assert_message == vallidation_error

    # TC03 üres kitöltés:
    email.clear()
    email.send_keys(" ")
    submit_button.click()

    assert_message2 = "Kérjük, töltse ki ezt a mezőt."
    validaton_err = driver.find_element_by_class_name("validation-error").text

    assert assert_message2 is not None
    assert assert_message2 == validaton_err


finally:
    pass
    driver.close()
