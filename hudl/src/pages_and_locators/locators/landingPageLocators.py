

from selenium.webdriver.common.by import By


class LandingPageLocators:

    LOGIN_DROPDOWN = (By.CSS_SELECTOR, 'div.mainnav__actions a[data-qa-id="login-select"]')
    HUDL_LOGIN = (By.CSS_SELECTOR, 'div.subnav__items a[data-qa-id="login-hudl"]')
    VOLLEYMETRICS_LOGIN = (By.CSS_SELECTOR, 'div.subnav__items a[data-qa-id="login-volleymetrics"]')
    WIMU_COUD_LOGIN = (By.CSS_SELECTOR, 'div.subnav__items a[data-qa-id="login-wimu"]')
    INSTAT_FOR_BASKETBALL_LOGIN = (By.CSS_SELECTOR, 'div.subnav__items a[data-qa-id="login-instat-basketball"]')
    INSTAT_FOR_ICE_HOCKEY_LOGIN = (By.CSS_SELECTOR, 'div.subnav__items a[data-qa-id="login-instat-icehockey"]')
    IQ_FOR_FOOTBALL_LOGIN = (By.CSS_SELECTOR, 'div.subnav__items a[data-qa-id="login-iq"]')
