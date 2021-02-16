# Сценарий тестирования отображения товаров 1.1.1
# Предусловия:
#   Перейти на страницу каталога
# Шаги:
# - Шаг 1, проверка отображения товаров в списке. Ожидаемый результат - наличие хотя бы одного товара на странице.
# - Шаг 2, проверка отображения элементов товара. Ожидаемый результат - наличие ссылки, изображения, заголовка и прочего хотя бы у одного товара на странице.
# - Шаг 3, проверка пагинации вперед. Ожидаемый результат - после нажатия на кнопку "Вперед" и обновления страницы отображается хотя бы один товар.
# - Шаг 4, проверка пагинации назад. Ожидаемый результат - после нажатия на кнопку "Назад" и обновления страницы отображается хотя бы один товар.

from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
product_class = 'product_pod'
product_image_link_selector = '.image_container img'
product_image_a_selector = '.image_container a'
product_header_link_selector = 'h3 a'
next_button_select = '.next'
prev_button_select = '.previous'


def test_items_view():
    try:
        # Arrange
        browser = webdriver.Chrome()
        # browser.implicitly_wait(5)
        browser.get(link)

        # get elements for step 1
        elements = browser.find_elements_by_class_name(product_class)
        # get first element for step 2
        first_element = browser.find_element_by_class_name(product_class)
        first_element_img = first_element.find_element_by_css_selector(product_image_link_selector).get_attribute('src')
        first_element_image_link = first_element.find_element_by_css_selector(product_image_a_selector).get_attribute(
            'href')
        first_element_header_link = first_element.find_element_by_css_selector(product_header_link_selector).get_attribute('href')
        first_element_header_text = first_element.find_element_by_css_selector(product_header_link_selector).text

        # Act
        # Переходим на следующую страницу, собираем количество товаров
        browser.find_element_by_css_selector(f"{next_button_select} a").click()
        time.sleep(1)
        elements_next_page = browser.find_elements_by_class_name(product_class)
        # Переходим на предыдующую страницу, собираем количество товаров
        browser.find_element_by_css_selector(f"{prev_button_select} a").click()
        time.sleep(1)
        elements_prev_page = browser.find_elements_by_class_name(product_class)

        # Assert
        assert len(elements) > 0, 'Init page does not contain items'
        assert len(first_element_img) > 0, 'First item on the page has no image'
        assert len(first_element_image_link) > 0, 'First item on the page has no image link'
        assert len(first_element_header_text) > 0, 'First item on the page has no header'
        assert len(first_element_header_link) > 0, 'First item on the page has no header link'
        assert len(elements_next_page) > 0, 'Next page does not contain items'
        assert len(elements_prev_page) > 0, 'Previous page does not contain items'

    finally:
        print('Success')
        browser.quit()


test_items_view()
