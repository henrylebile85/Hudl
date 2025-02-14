

# import pytest
# from pytest import mark
#
#
# from pframe1.src.pages.MyAccountSignedOut import MyAccountSignedOutRegister
# from pframe1.src.pages.MyAccountSignedIn import MyAccountSignedIn
# from pframe1.src.helpers.random_email_generating_helpers import generate_random_gmail_and_password
#
#
# @pytest.mark.usefixtures('init_driver')
# class TestLogIn:
#
#     @pytest.mark.login
#     @pytest.mark.tcid1
#     def test_login_happy_path(self):
#
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
