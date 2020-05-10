from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_xpath_form"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[3]/input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath("/html/body/div/form/div[4]/input")
    input4.send_keys("Russia")
    button1 = browser.find_element_by_xpath("//div[6]/button[3]")
    button1.click()

finally:
    time.sleep(30)
    browser.quit()

