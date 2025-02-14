

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
        self.sl.wait_until_element_is_visible(self.LOGIN_PASSWORD, 5)
        self.sl.wait_until_element_is_visible(self.FORGOT_PASSWORD_LINK, 5)
        self.sl.wait_until_element_is_visible(self.CREATE_ACCOUNT_LINK, 5)

    def click_on_continue_button(self):
        logger.debug("clicking 'continue' button.")
        self.sl.wait_and_click(self.CONTINUE_BTN)

    def click_on_edit_email(self):
        self.sl.wait_and_click(self.EDIT_USER_NAME)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_MSG, exp_err)

