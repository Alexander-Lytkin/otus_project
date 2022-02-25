from selenium.webdriver.common.by import By


class LoginAdminPage:
    LOGO = (By.XPATH, "//*[@id='header-logo']")
    PANEL_TITLE = (By.XPATH, "//*[@class='panel-title']")
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.ID, "input-password")
    FORGOTTEN_PASSWORD_BUTTON = (By.XPATH, "//*[@class='help-block']")
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
