import allure
from selenium.common import TimeoutException

from page_locators.signup_page_locator import SignupPageLocator as locator
from pages.signup_page import SignupPage
from steps.base_step_wait import BaseStepWait


class SignupStep(BaseStepWait):

    def __init__(self, driver):
        super().__init__(driver)
        self.signup_page = SignupPage(driver)

    @allure.step
    def click_phone_button(self):
        self.wait_for_element_to_be_visible_locator(locator.PHONE_FORM_BUTTON)
        button = self.signup_page.get_phone_button()
        button.click()

    @allure.step
    def click_email_button(self):
        self.wait_for_element_to_be_visible_locator(locator.EMAIL_FORM_BUTTON)
        button = self.signup_page.get_email_button()
        button.click()

    @allure.step
    def set_phone(self, phone):
        input = self.signup_page.get_phone_input()
        input.send_keys(phone)

    @allure.step
    def set_email(self, email):
        input = self.signup_page.get_email_input()
        input.send_keys(email)

    @allure.step
    def check_agree_checkbox(self):
        checkbox = self.signup_page.get_agree_checkbox()
        checkbox.click()

    @allure.step
    def select_currency(self, currency):
        select = self.signup_page.get_currency_select()
        select.click()
        locator.CURRENCY_OPTION[1] = locator.CURRENCY_OPTION[1].replace('%s', currency.upper())
        option = self.signup_page.get_currency_option()
        option.click()

    @allure.step
    def set_password(self, password):
        input = self.signup_page.get_password_input()
        input.send_keys(password)

    @allure.step
    def set_reenter_password(self, password):
        input = self.signup_page.get_reenter_password_input()
        input.send_keys(password)

    @allure.step
    def select_secret_question(self, question):
        select = self.signup_page.get_secret_question_select()
        select.click()
        locator.SECRET_QUESTION_OPTION[1] = locator.SECRET_QUESTION_OPTION[1].replace('%s', question)
        option = self.signup_page.get_secret_question_option()
        option.click()

    @allure.step
    def set_answer(self, answer):
        input = self.signup_page.get_answer_input()
        input.send_keys(answer)

    @allure.step
    def set_login(self, login):
        input = self.signup_page.get_login_input()
        input.send_keys(login)

    @allure.step
    def select_bonus(self, bonus):
        locator.BONUS_RADIO[1] = locator.BONUS_RADIO[1].replace('%s', bonus)
        radio = self.signup_page.get_reedem_bonus_radio()
        self.scroll_to_element(element=radio, arg="arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});")
        radio.click()

    @allure.step
    def set_address(self, address):
        input = self.signup_page.get_address_input()
        input.send_keys(address)

    @allure.step
    def select_country(self, country):
        select = self.signup_page.get_country_select()
        select.click()
        locator.COUNTRY_OPTION[1] = locator.COUNTRY_OPTION[1].replace('%s', country)
        option = self.signup_page.get_country_option()
        option.click()

    @allure.step
    def set_city(self, city):
        input = self.signup_page.get_city_input()
        input.send_keys(city)

    @allure.step
    def set_postalcode(self, postalcode):
        input = self.signup_page.get_postalcode_input()
        input.send_keys(postalcode)

    @allure.step
    def set_name(self, name):
        input = self.signup_page.get_name_input()
        input.send_keys(name)

    @allure.step
    def set_lastname(self, lastname):
        input = self.signup_page.get_lastname_input()
        input.send_keys(lastname)

    @allure.step
    def set_middlename(self, middlename):
        input = self.signup_page.get_middlename_input()
        input.send_keys(middlename)

    @allure.step
    def select_gender(self, gender):
        select = self.signup_page.get_gender_select()
        select.click()
        locator.GENDER_OPTION[1] = locator.GENDER_OPTION[1].replace('%s', gender)
        option = self.signup_page.get_gender_option()
        option.click()

    @allure.step
    def set_nickname(self, nickname):
        input = self.signup_page.get_nickname_input()
        input.send_keys(nickname)

    @allure.step
    def click_create_account_button(self):
        button = self.signup_page.get_create_account_button()
        button.click()

    @allure.step
    def get_existing_email_validation_text(self):
        try:
            self.wait_for_element_to_be_visible_locator(locator.EXISTING_EMAIL_INPUT_VALIDATION)
            error_e = self.signup_page.get_existing_email_validation()
            text = error_e.text
            return text.lower()
        except TimeoutException:
            return ''

    @allure.step
    def get_unchecked_agree_terms_validation_text(self):
        try:
            self.wait_for_element_to_be_visible_locator(locator.UNCHECKED_AGREE_TERMS_VALIDATION)
            error_e = self.signup_page.get_unchecked_agree_terms_validation()
            text = error_e.text
            return text.lower()
        except TimeoutException:
            return ''
