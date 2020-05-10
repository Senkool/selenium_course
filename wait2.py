import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    button = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    ok = browser.find_element_by_xpath("//button[@id='solve']").click()

finally:
    time.sleep(10)
    browser.quit()