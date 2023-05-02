from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):        
        assert "login" in self.url, "login is absent in current url"

    def should_be_login_form(self):        
        assert self.is_element_present(*LoginPageLocators.EMAIL_LINK), "Email link is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LINK), "Password link is not presented"

    def should_be_register_form(self):        
        assert self.is_element_present(*LoginPageLocators.NEW_EMAIL_LINK), "Email link is not presented"
        assert self.is_element_present(*LoginPageLocators.NEW_PASSWORD_LINK), "Password link is not presented"
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD_LINK), "Confirm password link is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.NEW_EMAIL_LINK)
        email_form.send_keys(email)
        new_password = self.browser.find_element(*LoginPageLocators.NEW_PASSWORD_LINK)
        new_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_LINK)
        confirm_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        button.click()
