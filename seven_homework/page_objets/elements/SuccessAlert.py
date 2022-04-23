from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class SuccessAlert(BasePage):
    SELF = (By.CSS_SELECTOR, ".alert-success")
    LOGIN = (By.LINK_TEXT, "login")
    SOPPING_CART = (By.PARTIAL_LINK_TEXT, "shopping cart")
    PRODUCT_COMPARISON = (By.LINK_TEXT, "product comparison")

    def click_login(self):
        self._click_in_element(self._element(self.SELF), self.LOGIN)

    def click_shopping_cart(self):
        self._click_in_element(self._element(self.SELF), self.SOPPING_CART)

    def click_product_comparison(self):
        self._click_in_element(self._element(self.SELF), self.PRODUCT_COMPARISON)
