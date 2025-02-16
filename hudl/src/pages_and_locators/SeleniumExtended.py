
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import time


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        ).send_keys(text)


    def wait_and_click(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        try:
            (WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
            ).click()
        except TimeoutException or StaleElementReferenceException or ElementClickInterceptedException:
            time.sleep(2)
            (WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            ).click()


    def wait_and_select_all_text_input(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.click()  # Ensure focus on element
            element.send_keys(Keys.CONTROL + 'a')  # Select all (Ctrl+A for Windows/Linux)
            element.send_keys(Keys.COMMAND + 'a')  # Select all (Cmd+A for Mac)

        except (TimeoutException, StaleElementReferenceException) as e:
            time.sleep(2)  # Retry after a brief wait
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.click()
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.COMMAND + 'a')


    def wait_and_delete_all_selected_text(self, locator, timeout=None):
        # Waits for an input or textarea field, sends Backspace keys until the text is fully deleted,
        # and waits until the field is empty before proceeding.
        timeout = timeout \
            if timeout else self.default_timeout

        try:
            # Wait for the input/textarea element to be visible
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )

            # Ensure it's an input or textarea element
            tag_name = element.tag_name.lower()
            if tag_name not in ["input", "textarea"]:
                raise ValueError("The element must be an <input> or <textarea> field.")

            # Get the current text length
            text_length = len(element.get_attribute("value"))

            # Send Backspace keys until all text is deleted
            for _ in range(text_length):
                element.send_keys(Keys.BACKSPACE)
                time.sleep(0.05)  # Small delay to ensure deletion

            # Wait until the text is completely removed
            WebDriverWait(self.driver, timeout).until(
                lambda driver: element.get_attribute("value") == ""
            )

        except (TimeoutException, StaleElementReferenceException):
            time.sleep(2)  # Retry after a brief wait
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )

            text_length = len(element.get_attribute("value"))

            for i in range(text_length):
                element.send_keys(Keys.BACKSPACE)
                time.sleep(0.05)

            WebDriverWait(self.driver, timeout).until(
                lambda driver: element.get_attribute("value") == ""
            )


    def wait_and_see(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        )

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value(locator, text))
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        )

    def wait_until_element_is_present(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))
        )



    def wait_for_element_to_disappear(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element(locator))
        )


    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element_text = elm.text
        return element_text


    def wait_and_ensure_same_page_is_visible(self, locator, timeout=None):
        time.sleep(3)
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        )

    def wait_until_url_changes(self, url, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.url_changes(url))
        )

    def wait_and_ensure_url_is_same(self, url, timeout=None):
        time.sleep(3)
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url))
        )

    def wait_and_confirm_url(self, url, timeout=None):
        time.sleep(2)
        timeout = timeout \
            if timeout else self.default_timeout
        try:
            (WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url))
        )
        except TimeoutException or StaleElementReferenceException or ElementClickInterceptedException:
            time.sleep(2)
            (WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url))
            )




