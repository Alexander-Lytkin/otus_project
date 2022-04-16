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
        logger = logging.getLogger(__name__)
    
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(f"/home/al/PycharmProjects/OTUS/otua_logger_with_allure/seven_homework/allure-results/{self.browser.test_name}.log")
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.ERROR)
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.5).move_to_element(element).click().perform()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def accept_alert(self):
        self.browser.switch_to.alert.accept()
