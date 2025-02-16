

from selenium.webdriver.common.by import By


class HudlLoginIDPageLocators:

    LOGIN_USER_NAME = (By.ID, 'username')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'div.c574b8c0d button[type="submit"]')
    ERRORS_CAUTION = (By.CSS_SELECTOR, 'div.input-wrapper span#error-element-username.ulp-input-error-message')
    LOGIN_ID_PAGE = (By.CSS_SELECTOR, 'main.login-id')




class HudlLoginThirdPartyPageLocators:
    CONTINUE_WITH_GOOGLE_BTN = (By.CSS_SELECTOR, 'button[data-provider="google"]')
    CONTINUE_WITH_FACEBOOK_BTN = (By.CSS_SELECTOR, 'button[data-provider="facebook"]')
    CONTINUE_WITH_APPLE_BTN = (By.CSS_SELECTOR, 'button[data-provider="apple"]')