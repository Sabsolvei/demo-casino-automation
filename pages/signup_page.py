from page_locators.signup_page_locator import SignupPageLocator as locator


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    def get_google_button(self):
        return self.driver.find_element(*locator.GOOGLE_BUTTON)

    def get_phone_button(self):
        return self.driver.find_element(*locator.PHONE_FORM_BUTTON)

    def get_email_button(self):
        return self.driver.find_element(*locator.EMAIL_FORM_BUTTON)

    def get_phone_input(self):
        return self.driver.find_element(*locator.PHONE_INPUT)

    def get_email_input(self):
        return self.driver.find_element(*locator.EMAIL_INPUT)

    def get_currency_select(self):
        return self.driver.find_element(*locator.CURRENCY_SELECT)

    def get_agree_checkbox(self):
        return self.driver.find_element(*locator.AGREE_CHECKBOX)

    def get_currency_option(self):
        return self.driver.find_element(*locator.CURRENCY_OPTION)

    def get_password_input(self):
        return self.driver.find_element(*locator.PASSWORD_INPUT)

    def get_reenter_password_input(self):
        return self.driver.find_element(*locator.REENTER_PASSWORD_INPUT)

    def get_secret_question_select(self):
        return self.driver.find_element(*locator.SECRET_QUESTION_SELECT)

    def get_secret_question_option(self):
        return self.driver.find_element(*locator.SECRET_QUESTION_OPTION)

    def get_answer_input(self):
        return self.driver.find_element(*locator.ANSWER_INPUT)

    def get_login_input(self):
        return self.driver.find_element(*locator.LOGIN_INPUT)

    def get_reedem_bonus_radio(self):
        return self.driver.find_element(*locator.BONUS_RADIO)

    def get_address_input(self):
        return self.driver.find_element(*locator.ADDRESS_INPUT)

    def get_country_select(self):
        return self.driver.find_element(*locator.COUNTRY_SELECT)

    def get_country_option(self):
        return self.driver.find_element(*locator.COUNTRY_OPTION)

    def get_city_input(self):
        return self.driver.find_element(*locator.CITY_INPUT)

    def get_postalcode_input(self):
        return self.driver.find_element(*locator.POSTALCODE_INPUT)

    def get_name_input(self):
        return self.driver.find_element(*locator.NAME_INPUT)

    def get_lastname_input(self):
        return self.driver.find_element(*locator.LASTNAME_INPUT)

    def get_middlename_input(self):
        return self.driver.find_element(*locator.MIDDLENAME_INPUT)

    def get_gender_select(self):
        return self.driver.find_element(*locator.GENDER_SELECT)

    def get_gender_option(self):
        return self.driver.find_element(*locator.GENDER_OPTION)

    def get_nickname_input(self):
        return self.driver.find_element(*locator.NICKNAME_INPUT)

    def get_create_account_button(self):
        return self.driver.find_element(*locator.CREATE_ACCOUNT_BUTTON)

#GET VALIDATIONS/ERRORS

    def get_existing_email_validation(self):
        return self.driver.find_element(*locator.EXISTING_EMAIL_INPUT_VALIDATION)

    def get_unchecked_agree_terms_validation(self):
        return self.driver.find_element(*locator.UNCHECKED_AGREE_TERMS_VALIDATION)
