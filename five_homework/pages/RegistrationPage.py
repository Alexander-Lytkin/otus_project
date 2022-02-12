from selenium.webdriver.common.by import By


class RegistrationPage:
    INPUT_FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
    INPUT_LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
    INPUT_EMAIL = (By.XPATH, "//*[@id='input-email']")
    INPUT_PHONE = (By.XPATH, "//*[@id='input-telephone']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='input-password']")
    INPUT_PASSWORD_CONFIRM = (By.XPATH, "//*[@id='input-confirm']")
    PRIVACY_POLICY = (By.XPATH, "//*[@type='checkbox']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
