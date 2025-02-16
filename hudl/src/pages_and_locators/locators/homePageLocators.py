

from selenium.webdriver.common.by import By

class HomePageLocators:

    UPLOAD= (By.CSS_SELECTOR, 'div.hui-globalnav__group a.hui-globalnav__upload--button-display')
    CALENDAR = (By.CSS_SELECTOR, 'div.hui-globalnav__group a[data-qa-id="webnav-globalnav-calendar"]')
    NOTIFICATIONS = (By.ID, 'notifications-link')
    MESSAGES = (By.CSS_SELECTOR, 'div.hui-globalnav__group a[data-qa-id="webnav-globalnav-messages"]')
    USER_MENU = (By.CSS_SELECTOR, 'div.hui-globalusermenu')
    HOME_PAGE = (By.ID, 'home-content')