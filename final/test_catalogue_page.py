from .pages.catalogue_page import CataloguePage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"


class TestCataloguePage:
    # Сценарий тестирования отображения товаров 1.1.1
    # @pytest.mark.skip(reason="not now")
    def test_guest_can_view_catalogue(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        # Act
        page.open()
        # Assert
        page.should_be_not_have_alerts()
        page.should_have_product()
        page.first_item_should_have_content()

    # @pytest.mark.skip(reason="not now")
    @pytest.mark.parametrize('page_number', ["1", "2", "3", "4"])
    def test_next_pagination_catalogue(self, browser, page_number):
        # Arrange
        sub_link = (link+'{}').format(f"?page={page_number}")
        page = CataloguePage(browser, sub_link)
        # Act
        page.open()
        page.go_to_next_page()
        page.should_be_not_have_alerts()
        catalogue_page = CataloguePage(browser, browser.current_url)
        # Assert
        catalogue_page.should_have_product()

    # @pytest.mark.skip(reason="not now")
    @pytest.mark.parametrize('page_number', [pytest.param("1", marks=pytest.mark.xfail), "2", "3", "4"])
    def test_prev_pagination_catalogue(self, browser, page_number):
        # Arrange
        sub_link = (link+'{}').format(f"?page={page_number}")
        page = CataloguePage(browser, sub_link)
        # Act
        page.open()
        page.go_to_prev_page()
        page.should_be_not_have_alerts()
        catalogue_page = CataloguePage(browser, browser.current_url)
        # Assert
        catalogue_page.should_have_product()

    # Сценарий добавления товара в корзину 1.2.1
    # @pytest.mark.skip(reason="not now")
    def test_view_button_to_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        # Act
        page.open()
        # Assert
        page.check_availability_buttons()

    # @pytest.mark.skip(reason="not now")
    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        # Act
        page.open()
        page.push_add_to_basket()
        # Assert
        page.check_update_basket()
