from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_css_selector("#num1").text
    second = browser.find_element_by_css_selector("#num2").text
    summ = int(first) + int(second)

    select = Select(browser.find_element_by_css_selector("#dropdown")).select_by_value(str(summ))

    button = browser.find_element_by_css_selector('.btn.btn-default').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
