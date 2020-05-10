from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/registration1.html")
    input1 = driver.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
    input2 = driver.find_element_by_css_selector(".first_block .second").send_keys("Ivanov")
    input3 = driver.find_element_by_css_selector(".first_block .third").send_keys("111@mail.ru")

    # находим кнопку
    button = driver.find_element_by_css_selector("button.btn").click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
	
	
