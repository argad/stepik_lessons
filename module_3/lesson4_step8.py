from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_name("firstname")
    x1.send_keys('max')

    x2 = browser.find_element_by_name("lastname")
    x2.send_keys('maxx')

    x3 = browser.find_element_by_name("email")
    x3.send_keys('qwe@qwe.qwe')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_css_selector("#file").send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
