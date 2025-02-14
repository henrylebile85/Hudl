

import random
import string
import logging as logger


# Generate Gmail separately
def generate_random_gmail(domain=None, email_prefix_main=None):

    if not domain:
        domain = "gmail.com"
    if not email_prefix_main:
        email_prefix_main = 'testuser'

    random_email_string_length = 10
    random_string_sub = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix_main + '+' + random_string_sub + '@' + domain

    return email



# Generate password separately
def generate_random_password(password = None):

    if not password:
        random_password_string_length = 19
        random_password_string = ''.join(random.choices(string.ascii_letters,
                                                        k=random_password_string_length))

        password = random_password_string + '!'

    logger.info(f'generated random password: {password}')

    return password



# Generate incorrect email separately
def generate_incorrect_email(email = None):

    if not email:
        random_email_string_length = 7
        random_email_string = ''.join(random.choices(string.ascii_letters,
                                                        k=random_email_string_length))

        email = random_email_string + '@'

    logger.info(f'generated an incorrect random email: {email}')

    return email

