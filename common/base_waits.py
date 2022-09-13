from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseWait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, condition, timeout=10):
        WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_element_to_be_visible_locator(self, locator, timeout=10):
        self.wait_for(EC.visibility_of_element_located(locator), timeout)
