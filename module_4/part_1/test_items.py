# Data generale
item_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
button_add_to_basket_locator = ".btn-add-to-basket"

basket_button_text_options = {
    "ru": "Добавить в корзину",
    "en": "Add to basket"
}

def test_button_add_to_basket_is_present(browser):
    # Arrange
    browser.get(item_page_link)

    # Act
    button_add_to_basket_text = browser.find_element_by_css_selector(button_add_to_basket_locator).text
    locale = browser.user_language.lower()
    print("Locale = " + locale)

    # Assert
    basket_button_text_assert = basket_button_text_options[locale]
    assert button_add_to_basket_text in basket_button_text_assert, \
        f"Text on the button is not correct."