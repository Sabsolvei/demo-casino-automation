from page_locators.confirm_email_page_locator import ConfirmEmailPageLocator as locator


class ConfirmEmailPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*locator.TITLE)

    def get_description(self):
        return self.driver.find_element(*locator.DESCRIPTION)

    def get_code_input(self):
        return self.driver.find_element(*locator.CODE_INPUT)

    def get_request_code_button(self):
        return self.driver.find_element(*locator.REQUEST_CODE_BUTTON)

    def get_verify_button(self):
        return self.driver.find_element(*locator.VERIFY_BUTTON)
#
