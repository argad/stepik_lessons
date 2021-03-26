from .base_page import BasePage
from .locators import BasketPageLocators
import re


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_items_in_basket()
        self.should_be_empty_basket_message()

    def should_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products added to the basket but should not be"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_CONTENT_TEXT).text, \
            "'Your basket is empty' message is not found"

    def should_have_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products have not added to the basket"

    def should_be_not_have_alerts(self):
        assert self.is_not_element_present(*BasketPageLocators.ALERT), \
            "Basket have alerts but should not be"

    def should_be_have_alerts(self):
        assert self.is_element_present(*BasketPageLocators.ALERT), \
            "Basket no have alerts"

    def change_basket_input(self):
        input_element = self.browser.find_element(*BasketPageLocators.BASKET_INPUT)
        input_element.clear()
        input_element.send_keys(2)
        quantity_button = self.browser.find_element(*BasketPageLocators.BASKET_INPUT_BUTTON)
        quantity_button.click()

    def should_have_correct_totals(self):
        basket_total = re.sub("[^0-9,.-]", "", self.browser.find_elements(*BasketPageLocators.BASKET_TOTALS)[0].text)
        basket_total = float(re.sub("[,]", ".", basket_total))
        delivery_price = re.sub("[^0-9,.-]", "", self.browser.find_elements(*BasketPageLocators.BASKET_TOTALS)[1].text)
        delivery_price = float(re.sub("[,]", ".", delivery_price))
        total_result = re.sub("[^0-9,.-]", "", self.browser.find_elements(*BasketPageLocators.BASKET_TOTALS)[2].text)
        total_result = float(re.sub("[,]", ".", total_result))
        assert (basket_total + delivery_price) == total_result, "Totals with discounts do not match"

    def delete_from_basket_button(self):
        delete_element = self.browser.find_element(*BasketPageLocators.DELETE_BUTTON)
        delete_element.click()

    def set_null_in_basket_button(self):
        input_element = self.browser.find_element(*BasketPageLocators.BASKET_INPUT)
        input_element.clear()
        input_element.send_keys(0)
        quantity_button = self.browser.find_element(*BasketPageLocators.BASKET_INPUT_BUTTON)
        quantity_button.click()
