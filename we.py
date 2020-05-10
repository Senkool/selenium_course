from selenium import webdriver
import time
import math

from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    num1 = int(num1)
    num2 = int(num2)
    sum1 = num1 + num2
    print("INT: ", sum1)
    sum1 = str(sum1)
    print("STR: ", sum1)
    dropdown = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    dropdown.select_by_visible_text(sum1)
    button = browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(10)
    browser.quit()



