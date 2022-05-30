import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(__name__)
        self.c_handler = logging.StreamHandler()
        self.f_handler = logging.FileHandler(f"allure-results/{self.browser.test_name}.log")
        self.c_handler.setLevel(logging.WARNING)
        self.f_handler.setLevel(logging.INFO)
        self.c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        self.f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.c_handler.setFormatter(self.c_format)
        self.f_handler.setFormatter(self.f_format)
        self.logger.addHandler(self.c_handler)
        self.logger.addHandler(self.f_handler)

    def _verify_link_presence(self, link_text):
        try:
            self.logger.info(f"Verify link presence {link_text}")
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            self.logger.info(f"Verify element presence {locator}")
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        self.logger.info(f"Element {locator}")
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        self.logger.info(f"Click on element {element}")
        ActionChains(self.browser).pause(0.5).move_to_element(element).click().perform()

    def _click(self, locator: tuple):
        self.logger.info(f"Click {locator}")
        element = self._element(locator)
        ActionChains(self.browser).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        self.logger.info(f"Click on element {element} in elements {locator}")
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def accept_alert(self):
        self.logger.info("Accept alert")
        self.browser.switch_to.alert.accept()
