import time
import os
import  math

from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"

try:


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))



    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    button_alert = browser.switch_to_alert()
    button_alert.accept()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    ok = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

finally:
    time.sleep(10)
    browser.quit()
