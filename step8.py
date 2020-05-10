import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    box = browser.find_element_by_xpath("//div[2]/label[1]")
    box.click()
    radio = browser.find_element_by_xpath("//label[contains(text(),'Robots rule')]")
    radio.click()
    # input3 = browser.find_element_by_xpath("//div[1]/div[3]/input")
    # input3.send_keys("qwer@hotmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

