

import pytest
from pytest import mark

from hudl.src.helpers.credential_management import get_credentials, get_password, get_username
from hudl.src.pages_and_locators.pages.landingPage import LandingPage
from hudl.src.pages_and_locators.pages.hudlLoginIDPage import HudlLoginIDPage
from hudl.src.pages_and_locators.pages.hudlLoginPasswordPage import HudlLoginPasswordPage
from hudl.src.pages_and_locators.pages.homePage import HomePage


@pytest.mark.usefixtures('init_driver')
class TestLogIn:

    HLodID_P_url = 'https://identity.hudl.com/u/login/identifier'
    HLPasswd_P_url = 'https://identity.hudl.com/u/login/password'
    Hom_P_url = 'https://www.hudl.com/home'

    @pytest.mark.login
    @pytest.mark.tcid1
    def test_login_happy_path(self):
        Land_P = LandingPage(self.driver)
        HLodID_P = HudlLoginIDPage(self.driver)
        HLPasswd_P = HudlLoginPasswordPage(self.driver)
        Hom_P = HomePage(self.driver)


        valid_email = get_username()
        valid_password = get_password()


        # Navigate to Hudl website
        Land_P.go_to_landing_page()

        # Click on Login Dropdown
        Land_P.click_log_in_dropdown()

        # Select hudl from the drop-down menu
        Land_P.click_hudl_login()

        # Enter a valid email address in the "Email" field and Click continue
        HLodID_P.wait_and_confirm_page()
        HLodID_P.input_login_username(valid_email)
        HLodID_P.click_on_continue_button()

        # Enter the correct password in the "Password" field and Click continue
        HLPasswd_P.wait_and_confirm_page()
        HLPasswd_P.input_login_password(valid_password)
        HLPasswd_P.wait_until_url_changes()

        # The user is successfully logged in and redirected to the homepage of Newcastle Jets FC.
        assert Hom_P.wait_and_confirm_page(), f'❌ Failed to login to {self.Hom_P_url}'
        assert Hom_P.verify_user_is_signed_in_visually() , f'❌ Failed to login to {self.Hom_P_url}'





#
#
#
#     @pytest.mark.login
#     @pytest.mark.tcid2
#     def test_login_edit(self):
#         my_account_out = MyAccountSignedOutRegister(self.driver)
#         my_account_in = MyAccountSignedIn(self.driver)
#
#         # go to my account
#         my_account_out.go_to_account()
#
#         # fill in email
#         rand_email = generate_random_gmail_and_password()
#         my_account_out.input_register_email_address(rand_email['email'])
#
#         # fill in password
#         rand_password = generate_random_gmail_and_password()
#         my_account_out.input_register_password(rand_password['password'])
#
#         # click register
#         my_account_out.click_register_button()
#
#         # verify user is registered
#         my_account_in.verify_user_is_signed_in_visually()
#
