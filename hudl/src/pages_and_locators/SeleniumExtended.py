
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
                EC.visibility_of_element_located(locator))
            ).click()
        except TimeoutException or StaleElementReferenceException or ElementClickInterceptedException:
            time.sleep(2)
            (WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            ).click()



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
            EC.text_to_be_present_in_element(locator, text))
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        )

    def wait_until_all_elements_are_visible(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))
        )

    def wait_for_element_to_disappear(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        (WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element(locator))
        )



    def wait_and_get_elements(self, locator, err=None, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        err = err if err else (f'unable to find elements located by "{locator}", '
                               f'after timeout of {timeout}')
        try:
            elements = (WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
            )
        except TimeoutException:
            raise TimeoutException()

        return elements


    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout \
            if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text
        return element_text
