from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 8).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    box = browser.find_element_by_id('answer')
    box.send_keys(y)
    button2 = browser.find_element_by_id('solve')
    button2.click()
    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')
    print(alert_text[-1])
    print('Finish')

finally:
    time.sleep(6)
    browser.quit()

