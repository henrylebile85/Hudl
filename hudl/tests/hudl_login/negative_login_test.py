

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

# @pytest.mark.login
    # @pytest.mark.tcid3
    # def test_login_non_existing_user(self):
    #     driver = self.driver
    #     Land_P = LandingPage(self.driver)
    #     HLodID_P = HudlLoginIDPage(self.driver)
    #     HLPasswd_P = HudlLoginPasswordPage(self.driver)
    #     Hom_P = HomePage(self.driver)
    #
    #     valid_email = get_username()
    #     valid_password = get_password()
    #     unregistered_email = generate_random_gmail()
    #     invalid_email = generate_incorrect_email()
    #     invalid_password = generate_random_password()
    #
    #     # Navigate to Hudl website
    #     Land_P.go_to_landing_page()
    #
    #     # Click on Login Dropdown
    #     Land_P.click_log_in_dropdown()
    #
    #     # Select hudl from the drop-down menu
    #     Land_P.click_hudl_login()
    #     Land_P.wait_until_url_changes()
    #
    #     # Enter a valid email address in the "Email" field and Click continue
    #     HLodID_P.wait_and_confirm_page()
    #     HLodID_P.wait_until_elements_are_visible()
    #     assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
    #     HLodID_P.input_login_username(valid_email)
    #     HLodID_P.click_on_continue_button()
    #     HLodID_P.wait_until_url_changes()
    #
    #     # Enter the correct password in the "Password" field and Click continue
    #     HLPasswd_P.wait_and_confirm_page()
    #     HLPasswd_P.wait_until_elements_are_visible()
    #     assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
    #     HLPasswd_P.input_login_password(valid_password)
    #     HLPasswd_P.click_on_continue_button()
    #     HLPasswd_P.wait_until_url_changes()
    #
    #     # The user is successfully logged in and redirected to the homepage of Newcastle Jets FC.
    #     Hom_P.wait_and_confirm_page()
    #     Hom_P.verify_user_is_signed_in_visually()
    #     assert driver.current_url == self.Hom_P_url, f'❌ user did not land in expected page {self.Hom_P_url}'
    #     expected_title = 'Home - Hudl'
    #     assert expected_title in driver.title, f"Expected title '{expected_title}' not found in page title: {self.driver.title}"
    #
    # @pytest.mark.login
    # @pytest.mark.tcid3
    # def test_login_non_existing_user(self):
    #     driver = self.driver
    #     Land_P = LandingPage(self.driver)
    #     HLodID_P = HudlLoginIDPage(self.driver)
    #     HLPasswd_P = HudlLoginPasswordPage(self.driver)
    #     Hom_P = HomePage(self.driver)
    #
    #     valid_email = get_username()
    #     valid_password = get_password()
    #     unregistered_email = generate_random_gmail()
    #     invalid_email = generate_incorrect_email()
    #     invalid_password = generate_random_password()
    #
    #     # Navigate to Hudl website
    #     Land_P.go_to_landing_page()
    #
    #     # Click on Login Dropdown
    #     Land_P.click_log_in_dropdown()
    #
    #     # Select hudl from the drop-down menu
    #     Land_P.click_hudl_login()
    #     Land_P.wait_until_url_changes()
    #
    #     # Enter a valid email address in the "Email" field and Click continue
    #     HLodID_P.wait_and_confirm_page()
    #     HLodID_P.wait_until_elements_are_visible()
    #     assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
    #     HLodID_P.input_login_username(valid_email)
    #     HLodID_P.click_on_continue_button()
    #     HLodID_P.wait_until_url_changes()
    #
    #     # Enter the correct password in the "Password" field and Click continue
    #     HLPasswd_P.wait_and_confirm_page()
    #     HLPasswd_P.wait_until_elements_are_visible()
    #     assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
    #     HLPasswd_P.input_login_password(valid_password)
    #     HLPasswd_P.click_on_continue_button()
    #     HLPasswd_P.wait_until_url_changes()
    #
    #     # The user is successfully logged in and redirected to the homepage of Newcastle Jets FC.
    #     Hom_P.wait_and_confirm_page()
    #     Hom_P.verify_user_is_signed_in_visually()
    #     assert driver.current_url == self.Hom_P_url, f'❌ user did not land in expected page {self.Hom_P_url}'
    #     expected_title = 'Home - Hudl'
    #     assert expected_title in driver.title, f"Expected title '{expected_title}' not found in page title: {self.driver.title}"
    #
    #
    # @pytest.mark.login
    # @pytest.mark.tcid3
    # def test_login_non_existing_user(self):
    #     driver = self.driver
    #     Land_P = LandingPage(self.driver)
    #     HLodID_P = HudlLoginIDPage(self.driver)
    #     HLPasswd_P = HudlLoginPasswordPage(self.driver)
    #     Hom_P = HomePage(self.driver)
    #
    #     valid_email = get_username()
    #     valid_password = get_password()
    #     unregistered_email = generate_random_gmail()
    #     invalid_email = generate_incorrect_email()
    #     invalid_password = generate_random_password()
    #
    #     # Navigate to Hudl website
    #     Land_P.go_to_landing_page()
    #
    #     # Click on Login Dropdown
    #     Land_P.click_log_in_dropdown()
    #
    #     # Select hudl from the drop-down menu
    #     Land_P.click_hudl_login()
    #     Land_P.wait_until_url_changes()
    #
    #     # Enter a valid email address in the "Email" field and Click continue
    #     HLodID_P.wait_and_confirm_page()
    #     HLodID_P.wait_until_elements_are_visible()
    #     assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
    #     HLodID_P.input_login_username(valid_email)
    #     HLodID_P.click_on_continue_button()
    #     HLodID_P.wait_until_url_changes()
    #
    #     # Enter the correct password in the "Password" field and Click continue
    #     HLPasswd_P.wait_and_confirm_page()
    #     HLPasswd_P.wait_until_elements_are_visible()
    #     assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
    #     HLPasswd_P.input_login_password(valid_password)
    #     HLPasswd_P.click_on_continue_button()
    #     HLPasswd_P.wait_until_url_changes()
    #
    #     # The user is successfully logged in and redirected to the homepage of Newcastle Jets FC.
    #     Hom_P.wait_and_confirm_page()
    #     Hom_P.verify_user_is_signed_in_visually()
    #     assert driver.current_url == self.Hom_P_url, f'❌ user did not land in expected page {self.Hom_P_url}'
    #     expected_title = 'Home - Hudl'
    #     assert expected_title in driver.title, f"Expected title '{expected_title}' not found in page title: {self.driver.title}"
    #
    #
    # @pytest.mark.login
    # @pytest.mark.tcid2
    # def test_login_edit(self):
    #     driver = self.driver
    #     Land_P = LandingPage(self.driver)
    #     HLodID_P = HudlLoginIDPage(self.driver)
    #     HLPasswd_P = HudlLoginPasswordPage(self.driver)
    #     Hom_P = HomePage(self.driver)
    #
    #
    #     valid_email = get_username()
    #     valid_password = get_password()
    #     unregistered_email = generate_random_gmail()
    #     invalid_email = generate_incorrect_email()
    #     invalid_password = generate_random_password()
    #
    #
    #     # Navigate to Hudl website
    #     Land_P.go_to_landing_page()
    #
    #     # Click on Login Dropdown
    #     Land_P.click_log_in_dropdown()
    #
    #     # Select hudl from the drop-down menu
    #     Land_P.click_hudl_login()
    #     Land_P.wait_until_url_changes()
    #
    #     # Enter an unregistered valid email address in the "Email" field and Click continue
    #     HLodID_P.wait_and_confirm_page()
    #     HLodID_P.wait_until_elements_are_visible()
    #     assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
    #     HLodID_P.input_login_username(unregistered_email)
    #     HLodID_P.click_on_continue_button()
    #     HLodID_P.wait_until_url_changes()
    #
    #     # Click Edit on the “Email” entry field
    #     HLPasswd_P.wait_and_confirm_page()
    #     HLPasswd_P.wait_until_elements_are_visible()
    #     assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
    #     HLPasswd_P.click_on_edit_email()
    #     HLPasswd_P.wait_until_url_changes()
    #
    #
    #     # Clear the existing credentials and Enter a Registered email address in the "Email" field and Click continue
    #     HLodID_P.wait_and_confirm_page()
    #     HLodID_P.wait_until_elements_are_visible()
    #     assert self.HLodID_P_url in driver.current_url, f' ❌ User is not on the login ID page, got {driver.current_url}'
    #     HLodID_P.wait_and_clear_text()
    #     HLodID_P.input_login_username(valid_email)
    #     HLodID_P.click_on_continue_button()
    #     HLodID_P.wait_until_url_changes()
    #
    #     # Enter the correct password in the "Password" field and Click continue
    #     HLPasswd_P.wait_and_confirm_page()
    #     HLPasswd_P.wait_until_elements_are_visible()
    #     assert self.HLPasswd_P_url in driver.current_url, f' ❌ User is not on the login Password page, got {driver.current_url}'
    #     HLPasswd_P.input_login_password(valid_password)
    #     HLPasswd_P.click_on_continue_button()
    #     HLPasswd_P.wait_until_url_changes()
    #
    #     # The user is successfully logged in and redirected to the homepage of Newcastle Jets FC.
    #     Hom_P.wait_and_confirm_page()
    #     Hom_P.verify_user_is_signed_in_visually()
    #     assert driver.current_url == self.Hom_P_url, f'❌ user did not land in expected page {self.Hom_P_url}'
    #     expected_title = 'Home - Hudl'
    #     assert expected_title in driver.title, f"Expected title '{expected_title}' not found in page title: {self.driver.title}"
    #
