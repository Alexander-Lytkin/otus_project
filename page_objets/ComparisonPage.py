from selenium.webdriver.common.by import By

from page_objets.BasePage import BasePage


class ComparisonPage(BasePage):
	CONTENT = (By.CSS_SELECTOR, "#content")
	ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
	
	def add_to_cart(self):
		self._click_in_element(self._element(self.CONTENT), self.ADD_TO_CART)
	
	def verify_product_link(self, product_name):
		self._verify_link_presence(product_name)
		return self
