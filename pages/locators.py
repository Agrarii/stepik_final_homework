from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_LINK = (By.NAME, "login-username")
    PASSWORD_LINK = (By.NAME, "login-password")
    NEW_EMAIL_LINK = (By.NAME, "registration-email")
    NEW_PASSWORD_LINK = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD_LINK = (By.NAME, "registration-password2")