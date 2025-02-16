import time

from hudl.src.pages_and_locators.locators.hudlLoginPasswordPageLocators import HudlLoginPasswordPageLocators
from hudl.src.pages_and_locators.SeleniumExtended import SeleniumExtended
import logging as logger



class HudlLoginPasswordPage(HudlLoginPasswordPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Login Password section

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password, 5)

    def wait_until_elements_are_visible(self):
        self.sl.wait_until_element_is_visible(self.LOGIN_PASSWORD)

    def click_on_continue_button(self):
        logger.debug("clicking 'continue' button.")
        self.sl.wait_and_click(self.CONTINUE_BTN)

    def click_on_edit_email(self):
        self.sl.wait_and_click(self.EDIT_USER_NAME)

    def wait_until_error_caution_is_present(self):
        self.sl.wait_until_element_is_present(self.ERROR_caution)

    def wait_until_error_caution_is_visible(self):
        self.sl.wait_until_element_is_visible(self.ERROR_caution)


    def wait_and_confirm_same_page(self):
        self.sl.wait_and_ensure_same_page_is_visible(self.PASSWORD_PAGE)
        self.sl.wait_and_ensure_url_is_same('https://identity.hudl.com/u/login/password')

    def wait_and_confirm_page(self):
        self.sl.wait_until_element_is_visible(self.PASSWORD_PAGE)
        self.sl.wait_and_confirm_url('https://identity.hudl.com/u/login/password')

    def wait_until_url_changes(self):
        self.sl.wait_until_url_changes('https://identity.hudl.com/u/login/password')



