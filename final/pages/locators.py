from selenium.webdriver.common.by import By


class CataloguePageLocators:
    PRODUCT = (By.CSS_SELECTOR, ".product_pod")
    PRODUCT_IMAGE_CLASS = (By.CSS_SELECTOR, ".thumbnail")
    PRODUCT_TITLE_CLASS = (By.CSS_SELECTOR, "h3 a")
    PRODUCT_BUTTON_CLASS = (By.CSS_SELECTOR, ".btn")
    PRODUCT_AVAILABLE_CLASS = (By.CSS_SELECTOR, ".availability")
    NEXT_PAGE = (By.CSS_SELECTOR, ".next a")
    PREV_PAGE = (By.CSS_SELECTOR, ".previous a")
    BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
    BASKET_UPDATE_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_CONTENT_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
