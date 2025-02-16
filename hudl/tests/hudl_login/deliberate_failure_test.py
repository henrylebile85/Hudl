

import pytest
from pytest import mark

from hudl.src.helpers.credential_management import get_credentials, get_password, get_username
from hudl.src.helpers.random_email_and_password_generating_helpers import generate_random_gmail, generate_random_password, generate_incorrect_email
from hudl.src.pages_and_locators.pages.landingPage import LandingPage
from hudl.src.pages_and_locators.pages.hudlLoginIDPage import HudlLoginIDPage
from hudl.src.pages_and_locators.pages.hudlLoginPasswordPage import HudlLoginPasswordPage
from hudl.src.pages_and_locators.pages.homePage import HomePage


@pytest.mark.usefixtures('init_driver')
class TestDeliberateFailure:

    HLodID_P_url = 'https://identity.hudl.com/u/login/identifier'
    HLPasswd_P_url = 'https://identity.hudl.com/u/login/password'
    Hom_P_url = 'https://www.hudl.com/home'
    error_message = 'Enter a valid email.'
    error_msg = 'Incorrect username or password.'


    @pytest.mark.login
    @pytest.mark.tcid7
    def test_deliberate_failure(self):
        driver = self.driver
        Land_P = LandingPage(self.driver)
        HLodID_P = HudlLoginIDPage(self.driver)
        HLPasswd_P = HudlLoginPasswordPage(self.driver)
        Hom_P = HomePage(self.driver)

        valid_email = get_username()
        valid_password = get_password()
        unregistered_email = generate_random_gmail()
        invalid_email = generate_incorrect_email()
        invalid_password = generate_random_password()


        # Navigate to hudl login page (https://www.hudl.com/login/).
        HLodID_P.go_to_login_page()

        # Enter a registered valid email address in the "Email" field and Click continue
        HLodID_P.wait_and_confirm_page()
        HLodID_P.wait_until_elements_are_visible()
        assert self.HLPasswd_P_url in driver.current_url, f' 🚨❌🚨Deliberate Failure {driver.current_url}🚨❌🚨'
        HLodID_P.input_login_username(valid_email)
        HLodID_P.click_on_continue_button()
        HLodID_P.wait_until_url_changes()
