

import pytest
from pytest import mark

from hudl.src.helpers.credential_management import get_credentials, get_password, get_username
from hudl.src.pages_and_locators.pages.landingPage import LandingPage
from hudl.src.pages_and_locators.pages.hudlLoginIDPage import HudlLoginIDPage
from hudl.src.pages_and_locators.pages.hudlLoginPasswordPage import HudlLoginPasswordPage
from hudl.src.pages_and_locators.pages.homePage import HomePage


@pytest.mark.usefixtures('init_driver')
class TestLogIn:

    @pytest.mark.login_test
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

        # Select hudl from the drop down menu
        Land_P.click_hudl_login()

        # Enter a valid email address in the "Email" field and Click continue
        HLodID_P.input_login_username(valid_email)
        HLodID_P.click_on_continue_button()




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
