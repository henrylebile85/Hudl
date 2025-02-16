
from hudl.src.pages_and_locators.locators.volleymetricsLoginIDPageLocators import VolleymetricsIDPageLocator
from hudl.src.pages_and_locators.SeleniumExtended import SeleniumExtended

import logging as logger



class HudlLoginIDPage(VolleymetricsIDPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    # Login user-name section

    def input_login_username(self, username):
        pass

    def click_on_continue_button(self):
        pass


    def wait_until_error_is_displayed(self, exp_err):
        pass

