from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_css_selector("h2 img")
    x = img.get_attribute("valuex")
    y = str(math.log(abs(12*math.sin(int(x)))))

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_css_selector("[value='robots']")
    radio.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
