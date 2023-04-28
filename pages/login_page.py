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