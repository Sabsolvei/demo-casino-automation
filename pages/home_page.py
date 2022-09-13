from page_locators.home_page_locator import HomePageLocator as locator


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_signup_button(self):
        return self.driver.find_element(*locator.SIGNUP_BUTTON)

    def get_gotit_button(self):
        return self.driver.find_element(*locator.GOTIT_BUTTON)
