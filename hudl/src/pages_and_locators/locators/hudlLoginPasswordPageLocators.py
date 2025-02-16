

from selenium.webdriver.common.by import By


class HudlLoginPasswordPageLocators:
    LOGIN_PASSWORD = (By.ID, 'password')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'div.c574b8c0d button[type="submit"]')
    EDIT_USER_NAME = (By.CSS_SELECTOR, 'div.c7e6cc6e7 a[data-link-name="edit-username"]')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href="/u/login/password-reset-start/prod-hudl-'
                                             'users-terraform/dvhvkdasv%40yahoo.com?state=hKFo2SAxSGkxaWJ'
                                             'YRG9Hby1JT2o3YUM5NzhpUzRLamZlTVdMN6Fur3VuaXZlcnNhbC1sb2dpbq'
                                             'N0aWTZIHVhYVNBWEI4UGhxU1p3ZWpocXF5dUJ0YjFBY3hiYmIto2NpZNkgbj'
                                             'EzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"]')
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/u/signup/identifier?state='
                                            'hKFo2SBQV0xVNXBWN1AzcDNIWkJ3LW5yV0xFT'
                                            'jRWdmtyRGtMaKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFBmVDF'
                                            'za2RRbTVvY1BscFUwYnVROHFCTm1OUzRrZ3Mxo2NpZNkgbj'
                                            'EzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"]')

    PASSWORD_PAGE = (By.CSS_SELECTOR, 'main.login')

    ERRORS_MSG = (By.ID, 'error-element-password')


error_msg = 'Incorrect username or password.'
