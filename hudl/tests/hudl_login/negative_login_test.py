

# import pytest
# from pytest import mark
#
# from pframe1.src.pages.MyAccountSignedOut import MyAccountSignedOutLogIn
#
#
# @pytest.mark.usefixtures('init_driver')
# class TestNegativeLogingIn:
#
#     @pytest.mark.login
#     @pytest.mark.tcid3
#     def test_login_non_existing_user(self):
#         user_name = 'bhjbsvgdjlbhjlvb'
#         user_password = 'vhvhvgdgusdgbu'
#
#         my_account = MyAccountSignedOutLogIn(self.driver)
#         # go to my account
#         my_account.go_to_account()
#         # type username
#         my_account.input_login_username(user_name)
#         # type password
#         my_account.input_login_password(user_password)
#         # click login
#         my_account.click_login_button()
#         # verify error message
#         expected_error = (f'Error: The username {user_name} is not registered on this site. '
#                                   f'If you are unsure of your username, try your email address instead.')
#
#         my_account.wait_until_error_is_displayed(expected_error)
#
#     @pytest.mark.login
#     @pytest.mark.tcid4
#     def test_login_non_existing_user(self):
#         user_name = 'bhjbsvgdjlbhjlvb'
#         user_password = 'vhvhvgdgusdgbu'
#
#         my_account = MyAccountSignedOutLogIn(self.driver)
#         # go to my account
#         my_account.go_to_account()
#         # type username
#         my_account.input_login_username(user_name)
#         # type password
#         my_account.input_login_password(user_password)
#         # click login
#         my_account.click_login_button()
#         # verify error message
#         expected_error = (f'Error: The username {user_name} is not registered on this site. '
#                           f'If you are unsure of your username, try your email address instead.')
#
#         my_account.wait_until_error_is_displayed(expected_error)
#
#
#     @pytest.mark.login
#     @pytest.mark.tcid5
#     def test_login_non_existing_user(self):
#         user_name = 'bhjbsvgdjlbhjlvb'
#         user_password = 'vhvhvgdgusdgbu'
#
#         my_account = MyAccountSignedOutLogIn(self.driver)
#         # go to my account
#         my_account.go_to_account()
#         # type username
#         my_account.input_login_username(user_name)
#         # type password
#         my_account.input_login_password(user_password)
#         # click login
#         my_account.click_login_button()
#         # verify error message
#         expected_error = (f'Error: The username {user_name} is not registered on this site. '
#                           f'If you are unsure of your username, try your email address instead.')
#
#         my_account.wait_until_error_is_displayed(expected_error)
#
#     @pytest.mark.login
#     @pytest.mark.tcid6
#     def test_login_non_existing_user(self):
#         user_name = 'bhjbsvgdjlbhjlvb'
#         user_password = 'vhvhvgdgusdgbu'
#
#         my_account = MyAccountSignedOutLogIn(self.driver)
#         # go to my account
#         my_account.go_to_account()
#         # type username
#         my_account.input_login_username(user_name)
#         # type password
#         my_account.input_login_password(user_password)
#         # click login
#         my_account.click_login_button()
#         # verify error message
#         expected_error = (f'Error: The username {user_name} is not registered on this site. '
#                           f'If you are unsure of your username, try your email address instead.')
#
#         my_account.wait_until_error_is_displayed(expected_error)
#
#     @pytest.mark.login
#     @pytest.mark.tcid7
#     def test_login_non_existing_user(self):
#         user_name = 'bhjbsvgdjlbhjlvb'
#         user_password = 'vhvhvgdgusdgbu'
#
#         my_account = MyAccountSignedOutLogIn(self.driver)
#         # go to my account
#         my_account.go_to_account()
#         # type username
#         my_account.input_login_username(user_name)
#         # type password
#         my_account.input_login_password(user_password)
#         # click login
#         my_account.click_login_button()
#         # verify error message
#         expected_error = (f'Error: The username {user_name} is not registered on this site. '
#                           f'If you are unsure of your username, try your email address instead.')
#
#         my_account.wait_until_error_is_displayed(expected_error)