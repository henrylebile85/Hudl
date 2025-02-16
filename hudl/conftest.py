


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import pytest_html
import os




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
            chrome_options.add_argument('--disable-dev-shm-usage')  # prevents shared memory issues
        # Set up the ChromeDriver using webdriver_manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # you can also use options to write it this way to set up ChromeDriver (below)


    elif browser in ('firefox', 'ff', 'headlessfirefox'):
        firefox_options = FirefoxOptions()
        if browser == 'headlessfirefox':
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('--headless')  # Ensures Firefox runs in headless mode
            firefox_options.add_argument('--disable-gpu')  # Prevents GPU-related crashes
            firefox_options.add_argument('--no-sandbox')  # Avoids security sandbox issues
            firefox_options.add_argument('--disable-dev-shm-usage')
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

    driver.quit() # Ensure the driver is closed after the tests



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Hook to add extra information (e.g., screenshots) to the HTML report and store both
    # the report and images in the same "Reports" folder.

    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        # Always add a sample URL to the report
        extras.append(pytest_html.extras.url("https://www.hudl.com/"))
        xfail = hasattr(report, "wasxfail")

        # Define the Reports directory
        reports_dir = os.path.join(os.getcwd(), "Reports")
        os.makedirs(reports_dir, exist_ok=True)

        # Check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = "init_driver" in item.fixturenames

            if is_frontend_test:
                # Save the screenshot in the Reports folder
                screen_shot_path = os.path.join(reports_dir, f"{item.name}.png")

                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screen_shot_path)

                # Add screenshot to the HTML report
                extras.append(pytest_html.extras.image(screen_shot_path))

                # Reference the screenshot in the XML report
                report.extra_xml = f'<image>{screen_shot_path}</image>'

    report.extras = extras



