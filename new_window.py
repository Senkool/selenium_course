import time
import os
import math

from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    redirect = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()
    browser.switch_to.window(browser.window_handles[1])

    print(browser.window_handles)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    ok = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()


finally:
    time.sleep(10)
    browser.quit()
