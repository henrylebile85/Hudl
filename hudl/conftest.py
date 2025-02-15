


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import pytest_html
import allure
import os
import subprocess
import sys
import time
import string
import random


# driver.implicitly_wait(10)



@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'safari', 'firefox', 'headlesschrome', 'ff', 'headlessfirefox']

    # Retrieve the browser type from environment variable
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set." )

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f'Provided browser {browser} is not one of the supported.'
                        f'Supported are: {supported_browsers}')


    # driver = None  # Initialize driver to ensure it's defined


    # Initialize the driver based on the browser
    if browser in ('chrome', 'ch', 'headlesschrome'):
        chrome_options = ChromeOptions()
        if browser == 'headlesschrome':
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')  # Ensures smooth headless operation
        # Set up the ChromeDriver using webdriver_manager
            chrome_options.add_argument('--disable-dev-shm-usage')

        # ✅ Fix: Avoid conflicting user data directory by setting a unique temp directory
        chrome_options.add_argument(f'--user-data-dir=/tmp/chrome-user-data-{os.getpid()}')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # you can also use options to write it this way to set up ChromeDriver (below)


    elif browser in ('firefox', 'ff', 'headlessfirefox'):
        firefox_options = FirefoxOptions()
        if browser == 'headlessfirefox':
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--no-sandbox')
            firefox_options.add_argument('--disable-gpu')  # Ensures smooth headless operation
        # Setup the GeckoDriver using webdriver_manager
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

    elif browser == 'safari':
        # Safari does not need a driver manager (it is pre-installed on macOS)
        driver = webdriver.Safari()

    if driver is None:
        raise Exception(f"Failed to initialize a driver for the browser: {browser}")

    # Pass the driver to the test class
    request.cls.driver = driver
    yield

    driver.quit() # Ensure the driver is closed after the tests5



# to set the environment variable
# For windows use any of the following, depending on what browser you want to run (no spaces in *=* )
# (set BROWSER=chrome)
# (set BROWSER=firefox)
# (set BROWSER=safari)

# For apple use any of the following, depending on what browser you want to run (no spaces in *=* )
# (export BROWSER=chrome)
# (export BROWSER=firefox)
# (export BROWSER=safari)





#### For: generating only pytest-html report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to add extra information (e.g., screenshots) to the HTML report and create a folder
    if it doesn't exist.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        # Always add a sample URL to the report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")

        # Check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = "init_driver" in item.fixturenames

            if is_frontend_test:
                # Define the Reports directory
                reports_dir = os.path.join(os.getcwd(), "Reports_Images_Failed_Tests")
                os.makedirs(reports_dir, exist_ok=True)

                # Save the screenshot in the Reports folder
                screen_shot_path = os.path.join(reports_dir, f"{item.name}.png")

                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screen_shot_path)

                # Add screenshot to the HTML report
                extras.append(pytest_html.extras.image(screen_shot_path))

                # Reference the screenshot in the XML report
                report.extra_xml = f'<image>{screen_shot_path}</image>'

    report.extras = extras



# to set the environment variable
# For windows use any of the following, depending on what browser you want to run (no spaces in *=* )
# (set RESULTS_DIR=then enter the absolute path of where you want the file to be stored e.g. reports )
# (set RESULTS_DIR=/Users/lbmacpro/Desktop/Framework/PFrame1/pframe1/pframe1/src/Reports)


# For apple use any of the following, depending on what browser you want to run (no spaces in *=* )
# (export RESULTS_DIR=/Users/lbmacpro/Desktop/Framework/PFrame1/pframe1/pframe1/src/Reports)

# Command for self-contained html
# pytest -m -s tcid12 --html=report.html --self-contained-html



