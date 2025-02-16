

import os
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()


def get_username():

    # Retrieves the username, prioritizing .env credentials first,
    # then falling back to system environment variables.
    # Raises an exception if no username is found.

    email = os.getenv('REGISTERED_EMAIL') or os.environ.get('REGISTERED_EMAIL')

    if not email:
        raise Exception("❌ Missing REGISTERED_EMAIL. Set it in a `.env` file or as an environment variable.")

    return email

def get_password():

    # Retrieves the password, prioritizing .env credentials first,
    # then falling back to system environment variables.
    # Raises an exception if no password is found.

    password = os.getenv('VALID_PASSWORD') or os.environ.get('VALID_PASSWORD')

    if not password:
        raise Exception("❌ Missing VALID_PASSWORD. Set it in a `.env` file or as an environment variable.")

    return password


def get_credentials():

    # Retrieves email and password, prioritizing .env credentials first,
    # then environment variables.
    # Raises an exception if either is missing.

    email = get_username()
    password = get_password()

    if not email or not password:
        raise Exception("❌ Missing credentials. Please set them in a `.env` file or as environment variables.")

    return email, password


# Example usage: runs only when credential_management.py is run
if __name__ == "__main__":
    try:
        email, password = get_credentials()
        print(f"✅ Credentials Loaded: {email} / {'*' * len(password)}")
    except Exception as e:
        print(e)
