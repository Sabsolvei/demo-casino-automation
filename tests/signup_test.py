import pytest

from steps.home_step import HomeStep
from steps.signup_step import SignupStep


@pytest.mark.usefixtures("driver", "class_setup")
class TestsSignup:

    @pytest.fixture
    def class_setup(self):
        self.home_step = HomeStep(self.driver)
        self.signup_step = SignupStep(self.driver)

    def test_register_new_user_succesfuly(self, dataset):
        self.home_step.click_button_gotit()
        self.home_step.click_button_signup()
        self.signup_step.click_email_button()
        #FALTA SELECCIONAR BANDERITA SI ES PHONE
        self.signup_step.check_agree_checkbox()
        self.signup_step.set_email(email=dataset['email'])
        self.signup_step.select_currency(currency=dataset['currency'])
        self.signup_step.set_password(password=dataset['password'])
        self.signup_step.set_reenter_password(password=dataset['reenter_password'])
        self.signup_step.select_secret_question(question=dataset['question'])
        self.signup_step.set_answer(answer=dataset['answer'])
        self.signup_step.set_login(login=dataset['login'])
        self.signup_step.select_bonus(bonus=dataset['bonus'])
        self.signup_step.set_address(address=dataset['address'])
        self.signup_step.select_country(country=dataset['country'])
        self.signup_step.set_city(city=dataset['city'])
        self.signup_step.set_postalcode(postalcode=dataset['postalcode'])
        self.signup_step.set_name(name=dataset['name'])
        self.signup_step.set_lastname(lastname=dataset['lastname'])
        self.signup_step.set_middlename(middlename=dataset['middlename'])
        self.signup_step.select_gender(gender=dataset['gender'])
        self.signup_step.set_nickname(nickname=dataset['nickname'])
        self.signup_step.click_create_account_button()

        pass

    def test_register_with_google_account_succesfuly(self):
        self.home_step.click_button_signup()
        pass

    def test_register_with_invalid_user_google_account(self):
        self.home_step.click_button_signup()
        pass

    def test_register_new_user_with_invalid_username(self):
        self.home_step.click_button_signup()
        pass
