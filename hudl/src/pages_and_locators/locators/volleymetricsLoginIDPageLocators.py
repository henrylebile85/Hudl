

from selenium.webdriver.common.by import By


class VolleymetricsIDPageLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'div.c574b8c0d button[type="submit"]')
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/u/signup/identifier?state='
                                            'hKFo2SBQV0xVNXBWN1AzcDNIWkJ3LW5yV0xFT'
                                            'jRWdmtyRGtMaKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFBmVDF'
                                            'za2RRbTVvY1BscFUwYnVROHFCTm1OUzRrZ3Mxo2NpZNkgbj'
                                            'EzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"]')

    ERRORS_MSG = (By.CSS_SELECTOR, 'div.input-wrapper span#error-element-username.ulp-input-error-message')

error_message = 'Enter a valid email.'