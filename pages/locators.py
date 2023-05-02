from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_MAIN_BTN = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    EMAIL_LINK = (By.NAME, "login-username")
    PASSWORD_LINK = (By.NAME, "login-password")
    NEW_EMAIL_LINK = (By.NAME, "registration-email")
    NEW_PASSWORD_LINK = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD_LINK = (By.NAME, "registration-password2")
    REGISTRATION_BTN = (By.NAME, "registration_submit")

class ProductPageLocators(object):
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")

class BasketPageLocators(object):
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_GOODS = (By.CSS_SELECTOR, ".thumbnail")
