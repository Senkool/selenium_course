import time
import math

from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    assert True

    check = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    radio = browser.find_element_by_xpath("//input[@id='robotsRule']").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()



