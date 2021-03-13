from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo={}"
default_promo_offer = "offer0"


class TestProductPage:
    @pytest.mark.skip(reason="not now")
    @pytest.mark.parametrize('promo_offer', [
        "?promo=offer0",
        "?promo=offer1",
        "?promo=offer2",
        "?promo=offer3",
        "?promo=offer4",
        "?promo=offer5",
        "?promo=offer6",
        pytest.param("?promo=offer7", marks=pytest.mark.xfail),
        "?promo=offer8",
        "?promo=offer9"
    ])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        page = ProductPage(browser, link.format(promo_offer))
        page.open()
        page.get_product_data()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_be_success_message()
        page.should_be_correct_product_in_success_message()
        page.should_be_basket()
        page.should_be_correct_price_in_basket()

    @pytest.mark.xfail(reason="wrong")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link.format(default_promo_offer))
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link.format(default_promo_offer))
        page.open()
        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="wrong")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link.format(default_promo_offer))
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_be_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

    @pytest.mark.testclass
    class TestUserAddToBasketFromProductPage:
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            email = str(time.time()) + "@fakemail.org"
            login_page.register_new_user(email=email, password=email)
            login_page.should_be_authorized_user()

        def test_user_cant_see_success_message(self, browser):
            # Arrange
            page = ProductPage(browser, link.format(default_promo_offer))
            page.open()
            # Assert
            page.should_not_be_success_message()

        def test_user_can_add_product_to_basket(self, browser):
            # Arrange
            page = ProductPage(browser, link.format(default_promo_offer))
            page.open()
            page.get_product_data()
            # Act
            page.add_product_to_basket()
            # Assert
            page.should_be_success_message()
            page.should_be_correct_product_in_success_message()
            page.should_be_basket()
            page.should_be_correct_price_in_basket()
