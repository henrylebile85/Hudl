from tokenize import endpats

from hudl.src.helpers.config_helpers import get_base_url
from hudl.src.pages_and_locators.locators.hudlLoginIDPageLocators import (HudlLoginIDPageLocators,
                                                                          HudlLoginThirdPartyPageLocators)
from hudl.src.pages_and_locators.SeleniumExtended import SeleniumExtended

import logging as logger



class HudlLoginIDPage(HudlLoginIDPageLocators,HudlLoginThirdPartyPageLocators):

    endpoint = '/login/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_login_page(self):
        base_url = get_base_url()
        login_page = base_url + self.endpoint
        logger.info(f'Going to: {login_page}')
        self.driver.get(login_page)


    # Login user-name section

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username, 5)

    def wait_and_clear_text(self):
        logger.debug("clearing existing text.")
        self.sl.wait_and_select_all_text_input(self.LOGIN_USER_NAME)
        self.sl.wait_and_delete_all_selected_text(self.LOGIN_USER_NAME)

    def click_on_continue_button(self):
        logger.debug("clicking 'continue' button.")
        self.sl.wait_and_click(self.CONTINUE_BTN)

    def wait_until_error_caution_is_present(self):
        self.sl.wait_until_element_is_present(self.ERRORS_CAUTION)

    def wait_until_error_caution_is_visible(self):
        self.sl.wait_until_element_is_visible(self.ERRORS_CAUTION)

    def wait_until_elements_are_visible(self):
        self.sl.wait_until_element_is_visible(self.CONTINUE_WITH_GOOGLE_BTN, 5)
        self.sl.wait_until_element_is_visible(self.CONTINUE_WITH_FACEBOOK_BTN, 5)
        self.sl.wait_until_element_is_visible(self.CONTINUE_WITH_APPLE_BTN, 5)

    def wait_and_confirm_same_page(self):
        self.sl.wait_and_ensure_same_page_is_visible(self.LOGIN_ID_PAGE)
        self.sl.wait_and_ensure_url_is_same('https://identity.hudl.com/u/login/identifier')

    def wait_and_confirm_page(self):
        self.sl.wait_until_element_is_visible(self.LOGIN_ID_PAGE)
        self.sl.wait_and_confirm_url('https://identity.hudl.com/u/login/identifier')

    def wait_until_url_changes(self):
        self.sl.wait_until_url_changes('https://identity.hudl.com/u/login/identifier')

