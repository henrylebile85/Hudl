

from selenium.webdriver.common.by import By


class HudlLoginPasswordPageLocators:
    LOGIN_PASSWORD = (By.ID, 'password')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'div.c574b8c0d button[type="submit"]')
    EDIT_USER_NAME = (By.CSS_SELECTOR, 'div.c7e6cc6e7 a[data-link-name="edit-username"]')
    PASSWORD_PAGE = (By.CSS_SELECTOR, 'main.login')

    ERROR_caution = (By.CSS_SELECTOR, 'span#error-element-password')
    ERRORS_MSG2 = (By.XPATH, "//div[@role='alert']//span")
    ERRORS_MSG3 = (By.XPATH, "(//span)[last()]")



