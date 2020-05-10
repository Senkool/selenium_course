from selenium import webdriver

import time
import math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_xpath("//img[@id='treasure']")
    img_att = img.get_attribute("valuex")
    print("Value: ", img_att)
    x = img_att
    y = calc(x)

    print("Ok: ", y)

    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    box = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    box.click()
    radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radio.click()
    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()




