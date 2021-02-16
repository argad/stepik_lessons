from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    button2 = browser.find_element_by_css_selector("#solve")
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
