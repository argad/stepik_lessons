from .pages.catalogue_page import CataloguePage
from .pages.basket_page import BasketPage
import pytest

basket_link = "http://selenium1py.pythonanywhere.com/ru/basket/"
catalogue_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"


class TestBasketPage:
    # Сценарий редактирования товара в корзине 2.1.1
    # Используем часть из прошлого теста, сначала добавляет товар в корзину
    # @pytest.mark.skip(reason="not now")
    def test_update_params_in_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, catalogue_link)
        # Act
        page.open()
        page.push_add_to_basket()

        page.check_update_basket()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_not_have_alerts()
        basket_page.change_basket_input()
        basket_page.should_be_have_alerts()
        basket_page.should_have_correct_totals()

    # Сценарий редактирования товара в корзине 2.2.1
    # Тестируем удаление
    @pytest.mark.xfail(reason="Кнопка удаления не работает")
    def test_delete_items_from_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, catalogue_link)
        # Act
        page.open()
        page.push_add_to_basket()

        page.check_update_basket()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_not_have_alerts()
        basket_page.delete_from_basket_button()
        basket_page.should_not_items_in_basket()

    def test_set_null_items_in_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, catalogue_link)
        # Act
        page.open()
        page.push_add_to_basket()

        page.check_update_basket()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_have_items_in_basket()
        basket_page.set_null_in_basket_button()
        basket_page.should_not_items_in_basket()
