from selenium.common import NoSuchElementException, TimeoutException

from common.base_steps import BaseStep
from common.base_waits import BaseWait


class BaseStepWait(BaseWait, BaseStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_element_present(self, locator, timeout=10):
        try:
            self.wait_for_element_to_be_visible(locator, timeout)
            return True
        except(NoSuchElementException, TimeoutException):
            return False

    def get_current_url(self):
        return self.driver.current_url
