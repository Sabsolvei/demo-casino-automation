from page_locators.home_page_locator import HomePageLocator as locator


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_signup_button(self):
        return self.driver.find_element(*locator.SIGNUP_BUTTON)

    def get_gotit_button(self):
        return self.driver.find_element(*locator.GOTIT_BUTTON)

    def get_theme_switcher_toggle(self):
        return self.driver.find_element(*locator.THEME_SWITCHER_TOGGLE)

    def get_theme_class(self):
        return self.driver.find_element(*locator.THEME_CLASS)

