import allure

from page_locators.home_page_locator import HomePageLocator as locator
from pages.home_page import HomePage
from steps.base_step_wait import BaseStepWait


class HomeStep(BaseStepWait):

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(driver)

    @allure.step
    def click_signup_button(self):
        self.wait_for_element_to_be_visible_locator(locator.SIGNUP_BUTTON)
        button = self.home_page.get_signup_button()
        button.click()

    @allure.step
    def click_gotit_button(self):
        self.wait_for_element_to_be_visible_locator(locator.GOTIT_BUTTON)
        button = self.home_page.get_gotit_button()
        button.click()

    @allure.step
    def click_theme_switcher_toggle(self):
        toggle = self.home_page.get_theme_switcher_toggle()
        toggle.click()

    @allure.step
    def get_theme_class(self):
        theme_class = self.home_page.get_theme_class()
        theme_class = theme_class.get_attribute("class")
        return theme_class

