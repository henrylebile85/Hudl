

from hudl.src.helpers.config_helpers import get_base_url
from hudl.src.pages_and_locators.SeleniumExtended import SeleniumExtended
from hudl.src.pages_and_locators.locators.landingPageLocators import LandingPageLocators

import logging as logger



class LandingPage(LandingPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_landing_page(self):
        base_url = get_base_url()
        landing_page_url = base_url
        logger.info(f'Going to: {landing_page_url}')
        self.driver.get(landing_page_url)

    def click_log_in_dropdown(self):
        self.sl.wait_and_click(self.LOGIN_DROPDOWN)

    def click_hudl_login(self):
        self.sl.wait_and_click(self.HUDL_LOGIN)

    def click_volleymetrics_login(self):
        self.sl.wait_and_click(self.VOLLEYMETRICS_LOGIN)

    def click_wimu_cloud_login(self):
        self.sl.wait_and_click(self.WIMU_COUD_LOGIN)

    def click_instat_for_basketball_login(self):
        self.sl.wait_and_click(self.INSTAT_FOR_BASKETBALL_LOGIN)

    def click_instat_for_ice_hockey_login(self):
        self.sl.wait_and_click(self.INSTAT_FOR_ICE_HOCKEY_LOGIN)

    def click_iq_for_football_login(self):
        self.sl.wait_and_click(self.IQ_FOR_FOOTBALL_LOGIN)

    def wait_until_url_changes(self):
        self.sl.wait_until_url_changes('https://www.hudl.com/')


