

import pytest
from pytest import mark

from hudl.src.helpers.credential_management import get_credentials, get_password, get_username
from hudl.src.helpers.random_email_and_password_generating_helpers import generate_random_gmail, generate_random_password, generate_incorrect_email
from hudl.src.pages_and_locators.pages.landingPage import LandingPage
from hudl.src.pages_and_locators.pages.hudlLoginIDPage import HudlLoginIDPage
from hudl.src.pages_and_locators.pages.hudlLoginPasswordPage import HudlLoginPasswordPage
from hudl.src.pages_and_locators.pages.homePage import HomePage


@pytest.mark.usefixtures('init_driver')
class TestNegativeLogingIn:

    HLodID_P_url = 'https://identity.hudl.com/u/login/identifier'
    HLPasswd_P_url = 'https://identity.hudl.com/u/login/password'
    Hom_P_url = 'https://www.hudl.com/home'
    error_message = 'Enter a valid email.'
    error_msg = 'Incorrect username or password.'

    @pytest.mark.login
    @pytest.mark.tcid3
    def test_invalid_login_registered_email_and_incorrect_password(self):
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
        assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
        HLodID_P.input_login_username(valid_email)
        HLodID_P.click_on_continue_button()
        HLodID_P.wait_until_url_changes()

        # Enter an incorrect password in the "Password" field and Click continue
        HLPasswd_P.wait_and_confirm_page()
        HLPasswd_P.wait_until_elements_are_visible()
        assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
        HLPasswd_P.input_login_password(invalid_password)
        HLPasswd_P.click_on_continue_button()
        HLPasswd_P.wait_and_confirm_same_page()

        # The system displays an appropriate error message
        HLPasswd_P.wait_until_error_caution_is_present()


        # The user is not logged in.
        HLPasswd_P.wait_and_confirm_same_page()
        assert self.HLPasswd_P_url in driver.current_url, f'❌ user did not remain on page {self.HLPasswd_P_url}'


    @pytest.mark.login
    @pytest.mark.tcid4
    def test_invalid_login_unregistered_email_and_correct_password(self):
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

        # Enter an unregistered valid email address in the "Email" field and Click continue
        HLodID_P.wait_and_confirm_page()
        HLodID_P.wait_until_elements_are_visible()
        HLodID_P.input_login_username(unregistered_email)
        HLodID_P.click_on_continue_button()
        HLodID_P.wait_until_url_changes()

        # Enter the correct password in the "Password" field and Click continue
        HLPasswd_P.wait_and_confirm_page()
        HLPasswd_P.wait_until_elements_are_visible()
        assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
        HLPasswd_P.input_login_password(valid_password)
        HLPasswd_P.click_on_continue_button()
        HLPasswd_P.wait_and_confirm_same_page()

        # The system displays an error caution
        HLPasswd_P.wait_until_error_caution_is_present()

        # The user is not logged in.
        HLPasswd_P.wait_and_confirm_same_page()
        assert self.HLPasswd_P_url in driver.current_url, f'❌ user did not remain on page {self.HLPasswd_P_url}'


    @pytest.mark.login
    @pytest.mark.tcid5
    def test_invalid_login_invalid_email(self):
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

        # Enter an invalid email address in the "Email" field and Click continue
        HLodID_P.wait_and_confirm_page()
        HLodID_P.wait_until_elements_are_visible()
        assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
        HLodID_P.input_login_username(invalid_email)
        HLodID_P.click_on_continue_button()
        HLodID_P.wait_and_confirm_same_page()

        # The system displays an error caution
        HLodID_P.wait_until_error_caution_is_visible()

        # The user is not logged in.
        HLodID_P.wait_and_confirm_same_page()
        assert self.HLodID_P_url in driver.current_url, f'❌ user did not remain on page {self.HLodID_P_url}'


    @pytest.mark.login
    @pytest.mark.tcid6
    def test_invalid_login_empty_credentials(self):
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

        # click the continue button
        HLodID_P.click_on_continue_button()
        HLodID_P.wait_and_confirm_same_page()
        assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'

        # Enter an unregistered email address in the "Email" field and Click continue
        HLodID_P.input_login_username(unregistered_email)
        HLodID_P.click_on_continue_button()
        HLodID_P.wait_until_url_changes()
        HLPasswd_P.wait_and_confirm_page()
        HLPasswd_P.wait_until_elements_are_visible()
        assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
        HLPasswd_P.click_on_continue_button()
        HLPasswd_P.wait_and_confirm_same_page()

        # The user remains on the corresponding login password page where the data entry was empty
        HLPasswd_P.wait_and_confirm_same_page()

        # The user is not logged in.
        assert self.HLPasswd_P_url in driver.current_url, f'❌ user did not remain on page {self.HLPasswd_P_url}'