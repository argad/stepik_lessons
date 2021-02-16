from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    button2 = browser.find_element_by_css_selector(".btn.btn-primary")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
