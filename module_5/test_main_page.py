from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    @pytest.mark.loginquest
    class TestLoginFromMainPage:
        def test_guest_can_go_to_login_page(self, browser):
            page = MainPage(browser, link)
            page.open()
            page.should_be_login_link()

        def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
            page = MainPage(browser, link)
            page.open()
            page.go_to_basket_page()
            basket_page = BasketPage(browser, browser.current_url)
            basket_page.should_be_empty_basket()



