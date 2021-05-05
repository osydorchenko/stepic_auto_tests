from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name('button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    box = browser.find_element_by_id('answer')
    box.send_keys(y)
    button2 = browser.find_element_by_tag_name('button')
    button2.click()

finally:
    time.sleep(6)
    browser.quit()
