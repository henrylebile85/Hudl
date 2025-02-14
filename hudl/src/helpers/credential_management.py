

import os


def get_username():
    email = os.environ.get('REGISTERED_EMAIL')

    if not email:
        raise Exception("Missing credentials in GitHub Secrets.")

    return email



def get_password():
    password = os.environ.get('VALID_PASSWORD')

    if not password:
        raise Exception("Missing credentials in GitHub Secrets.")

    return password




def get_credentials():
    # Retrieve credentials from GitHub Secrets.
    email = os.environ.get("REGISTERED_EMAIL")
    password = os.environ.get("VALID_PASSWORD")

    if not email or not password:
        raise Exception("Missing credentials in GitHub Secrets.")

    return email, password