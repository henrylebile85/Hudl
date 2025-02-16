
from hudl.src.pages_and_locators.locators.homePageLocators import HomePageLocators
from hudl.src.pages_and_locators.SeleniumExtended import SeleniumExtended

import logging as logger



class HomePage(HomePageLocators):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def verify_user_is_signed_in_visually(self):
        self.sl.wait_until_element_is_visible(self.UPLOAD)
        self.sl.wait_until_element_is_visible(self.CALENDAR)
        self.sl.wait_until_element_is_visible(self.NOTIFICATIONS)
        self.sl.wait_until_element_is_visible(self.MESSAGES)
        self.sl.wait_until_element_is_visible(self.USER_MENU)


    def wait_and_confirm_same_page(self):
        self.sl.wait_and_ensure_same_page_is_visible(self.HOME_PAGE)
        self.sl.wait_and_ensure_url_is_same('https://www.hudl.com/home')

    def wait_and_confirm_page(self):
        self.sl.wait_until_element_is_visible(self.HOME_PAGE)
        self.sl.wait_and_confirm_url('https://www.hudl.com/home')

