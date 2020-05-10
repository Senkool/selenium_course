from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_xpath("//button[@id='verify']").click()

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
