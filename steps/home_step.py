from page_locators.home_page_locator import HomePageLocator as locator
from pages.home_page import HomePage
from steps.base_step_wait import BaseStepWait


class HomeStep(BaseStepWait):

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(driver)

    def click_button_signup(self):
        self.wait_for_element_to_be_visible_locator(locator.SIGNUP_BUTTON)
        button = self.home_page.get_signup_button()
        button.click()

    def click_button_gotit(self):
        self.wait_for_element_to_be_visible_locator(locator.GOTIT_BUTTON)
        button = self.home_page.get_gotit_button()
        button.click()