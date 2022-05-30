import time
from selenium.webdriver.common.by import By

from page_objets.BasePage import BasePage


class ProductPage(BasePage):
	WISH_LIST_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
	ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
	ADD_TO_COMPARISON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
	
	def add_to_wish_list(self):
		self._click(self.WISH_LIST_BUTTON)
	
	def add_to_cart(self):
		time.sleep(1)  # Page loading problem
		self._click(self.ADD_TO_CART_BUTTON)
	
	def add_to_comparison(self):
		self._click(self.ADD_TO_COMPARISON)
