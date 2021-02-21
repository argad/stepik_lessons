# Сценарий тестирования отображения товаров 1.1.1
# Предусловия:
#   Перейти на страницу каталога
# Шаги:
# - Шаг 1, проверка отображения товаров в списке. Ожидаемый результат - наличие хотя бы одного товара на странице.
# - Шаг 2, проверка отображения элементов товара. Ожидаемый результат - наличие ссылки, изображения, заголовка и прочего хотя бы у одного товара на странице.
# - Шаг 3, проверка пагинации вперед. Ожидаемый результат - после нажатия на кнопку "Вперед" и обновления страницы отображается хотя бы один товар.
# - Шаг 4, проверка пагинации назад. Ожидаемый результат - после нажатия на кнопку "Назад" и обновления страницы отображается хотя бы один товар.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
product_class = '.product_pod'
product_image_link_selector = '.image_container img'
product_image_a_selector = '.image_container a'
product_header_link_selector = 'h3 a'
next_button_select = '.next'
prev_button_select = '.previous'
expected_element_class = 'page_inner'


def test_items_view():
    try:
        # Arrange
        browser = webdriver.Chrome()
        # browser.implicitly_wait(5)
        browser.get(link)

        # get elements for step 1
        page_goods = browser.find_elements_by_css_selector(product_class)
        # get first element for step 2
        page_good = browser.find_element_by_css_selector(product_class)
        page_good_img = page_good.find_element_by_css_selector(product_image_link_selector).get_attribute('src')
        page_good_image_link = page_good.find_element_by_css_selector(product_image_a_selector).get_attribute(
            'href')
        page_good_header_link = page_good.find_element_by_css_selector(product_header_link_selector).get_attribute('href')
        page_good_header_text = page_good.find_element_by_css_selector(product_header_link_selector).text

        # Act

        # Assert
        assert len(page_goods) > 0, 'Init page does not contain items'
        assert len(page_good_img) > 0, 'First item on the page has no image'
        assert len(page_good_image_link) > 0, 'First item on the page has no image link'
        assert len(page_good_header_text) > 0, 'First item on the page has no header'
        assert len(page_good_header_link) > 0, 'First item on the page has no header link'

    finally:
        print('Success')
        browser.quit()

def test_navigation_view():
    try:
        # Arrange
        browser = webdriver.Chrome()
        # browser.implicitly_wait(5)
        browser.get(link)

        # Act
        # Переходим на следующую страницу, собираем количество товаров
        browser.find_element_by_css_selector(f"{next_button_select} a").click()
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, expected_element_class))
        )
        goods_next_page = browser.find_elements_by_css_selector(product_class)
        # Переходим на предыдующую страницу, собираем количество товаров
        browser.find_element_by_css_selector(f"{prev_button_select} a").click()
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, expected_element_class))
        )
        goods_prev_page = browser.find_elements_by_css_selector(product_class)

        # Assert
        assert len(goods_next_page) > 0, 'Next page does not contain items'
        assert len(goods_prev_page) > 0, 'Previous page does not contain items'

    finally:
        print('Success')
        browser.quit()


test_items_view()
test_navigation_view()
