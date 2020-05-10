import time
import os

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    Fname = browser.find_element_by_xpath("//input[@placeholder='Enter first name']").send_keys("Ivan")
    Lname = browser.find_element_by_xpath("//input[@placeholder='Enter last name']").send_keys("Petrov")
    Mail = browser.find_element_by_xpath("//input[@placeholder='Enter email']").send_keys("ivanpetron@mail.ru")

    element = browser.find_element_by_xpath("//input[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

finally:
    time.sleep(10)
    browser.quit()





