import allure

from pages.confirm_email_page import ConfirmEmailPage

from steps.base_step_wait import BaseStepWait


class ConfirmEmailStep(BaseStepWait):

    def __init__(self, driver):
        super().__init__(driver)
        self.confirm_page = ConfirmEmailPage(driver)

    @allure.step
    def get_title_text(self):
        text = self.confirm_page.get_title().text.lower()
        return text

    @allure.step
    def get_description_text(self):
        text = self.confirm_page.get_description().text.lower()
        return text

    @allure.step
    def visibility_code_input(self):
        visible = self.is_element_present(self.confirm_page.get_code_input())
        return visible

    @allure.step
    def visibility_verify_button(self):
        visible = self.is_element_present(self.confirm_page.get_verify_button())
        return visible

    @allure.step
    def visibility_request_code_button(self):
        visible = self.is_element_present(self.confirm_page.get_request_code_button())
        return visible
