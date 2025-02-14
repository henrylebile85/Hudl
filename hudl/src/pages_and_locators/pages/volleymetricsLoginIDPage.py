
from hudl.src.pages_and_locators.locators.volleymetricsLoginIDPageLocators import VolleymetricsIDPageLocator
from hudl.src.pages_and_locators.SeleniumExtended import SeleniumExtended

import logging as logger



class HudlLoginIDPage(VolleymetricsIDPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    # Login user-name section

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username, 5)

    def click_on_continue_button(self):
        logger.debug("clicking 'continue' button.")
        self.sl.wait_and_click(self.CONTINUE_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_MSG, exp_err)
