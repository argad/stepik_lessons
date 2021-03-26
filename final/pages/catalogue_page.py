from .base_page import BasePage
from .locators import CataloguePageLocators


class CataloguePage(BasePage):
    def should_have_product(self):
        assert self.is_element_present(*CataloguePageLocators.PRODUCT), "No products found."

    def first_item_should_have_content(self):
        first_element = self.browser.find_element(*CataloguePageLocators.PRODUCT)
        self.first_item_should_have_image(first_element)
        self.first_item_should_have_title(first_element)
        self.first_item_should_have_button(first_element)

    def first_item_should_have_image(self, element):
        assert self.is_sub_element_present(element, *CataloguePageLocators.PRODUCT_IMAGE_CLASS), \
            "Product on the catalogue has no image."

    def first_item_should_have_title(self, element):
        assert self.is_sub_element_present(element, *CataloguePageLocators.PRODUCT_TITLE_CLASS), \
            "Product on the catalogue has no title."

    def first_item_should_have_button(self, element):
        assert self.is_sub_element_present(element, *CataloguePageLocators.PRODUCT_BUTTON_CLASS), \
            "Product on the catalogue has no button."

    def go_to_next_page(self):
        link = self.browser.find_element(*CataloguePageLocators.NEXT_PAGE)
        link.click()

    def go_to_prev_page(self):
        link = self.browser.find_element(*CataloguePageLocators.PREV_PAGE)
        link.click()

    def push_add_to_basket(self):
        link = self.browser.find_element(*CataloguePageLocators.PRODUCT)\
            .find_element(*CataloguePageLocators.PRODUCT_BUTTON_CLASS)
        link.click()

    def get_availability_status(self):
        products = self.browser.find_elements(*CataloguePageLocators.PRODUCT)
        try:
            for product in products:
                availability_class = product.find_element_by_css_selector(
                    CataloguePageLocators.PRODUCT_BUTTON_CLASS[1]).get_attribute("class")
                button_class = product.find_element_by_css_selector(
                    CataloguePageLocators.PRODUCT_BUTTON_CLASS[1]).get_attribute("class")
                if ('outofstock' in availability_class) and ('disabled' not in button_class):
                    raise Exception('exception')
        except Exception:
            return False
        return True

    def check_availability_buttons(self):
        assert self.get_availability_status(), 'Product add button to basket is available but should not'

    def check_update_basket(self):
        alert_price_value = self.browser.find_element(*CataloguePageLocators.BASKET_UPDATE_ALERT).text
        basket_price_value = \
            self.browser.find_element(*CataloguePageLocators.BASKET_MINI).text.split(':')[1].split('\n')[0].strip()
        assert alert_price_value == basket_price_value, \
            f"Price in the alert and price in the basket should match. Got alert_price_value={alert_price_value} and " \
            f"basket_price_value={basket_price_value} instead"

    def should_be_not_have_alerts(self):
        assert self.is_not_element_present(*CataloguePageLocators.ALERT), \
            "Catalogue have alerts but should not be"
