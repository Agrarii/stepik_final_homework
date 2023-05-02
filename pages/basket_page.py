from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), \
            "Goods is presented, but would not be"

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket isn't empty'"