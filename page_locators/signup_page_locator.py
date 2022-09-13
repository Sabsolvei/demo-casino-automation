from selenium.webdriver.common.by import By


class SignupPageLocator(object):
    GOOGLE_BUTTON = (By.XPATH, "//i[@class='icon-google']/ancestor::a[contains(@class,'google')]")

    PHONE_FORM_BUTTON = (By.XPATH, "//div[@class='selectric-scroll']/ul/li[text()='Phone']")
    EMAIL_FORM_BUTTON = (By.XPATH, "//div[@class='selectric-scroll']/ul/li[text()='E-mail']")

    PHONE_INPUT = (By.XPATH, "//label[text()='Phone number']/following-sibling::div//input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::div/input")

    AGREE_CHECKBOX = (By.XPATH, "//div[contains(@class,'form__input--checkbox')]")

    CURRENCY_SELECT = (By.XPATH, "//label[text()='Currency']/following-sibling::div")
    CURRENCY_OPTION = [By.XPATH, "//label[text()='Currency']/following-sibling::div//ul/li[contains(text(),'%s')]"]
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/following-sibling::div//input")
    REENTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Reenter password']/following-sibling::div//input")
    SECRET_QUESTION_SELECT = (By.XPATH, "//label[text()='Secret Question']/following-sibling::div/div")
    SECRET_QUESTION_OPTION = [By.XPATH,
                              "//label[text()='Secret Question']/following-sibling::div/div//ul/li[contains(text(),'%s')]"]
    ANSWER_INPUT = (By.XPATH, "//label[text()='Answer']/following-sibling::div/input")
    LOGIN_INPUT = (By.XPATH, "//label[text()='Login']/following-sibling::div/input")

    BONUS_RADIO = [By.XPATH, "//span[contains(text(),'%s')]/.."]

    ADDRESS_INPUT = (By.XPATH, "//label[text()='Address']/following-sibling::div/input")
    COUNTRY_SELECT = (By.XPATH, "//label[text()='Country']/following-sibling::div/div")
    COUNTRY_OPTION = [By.XPATH, "//label[text()='Country']/following-sibling::div/div//ul/li[contains(text(),'%s')]"]
    CITY_INPUT = (By.XPATH, "//label[text()='City']/following-sibling::div/input")
    POSTALCODE_INPUT = (By.XPATH, "//label[text()='Postal code']/following-sibling::div/input")
    NAME_INPUT = (By.XPATH, "//label[text()='Name']/following-sibling::div/input")
    LASTNAME_INPUT = (By.XPATH, "//label[text()='Last name']/following-sibling::div/input")
    MIDDLENAME_INPUT = (By.XPATH, "//label[text()='Middle name']/following-sibling::div/input")
    GENDER_SELECT = (By.XPATH, "//label[text()='Gender']/following-sibling::div/div")
    GENDER_OPTION = [By.XPATH, "//label[text()='Gender']/following-sibling::div/div//ul/li[contains(text(),'%s')]"]
    NICKNAME_INPUT = (By.XPATH, "//label[text()='Nickname']/following-sibling::div/input")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button/span[text()='Create account']")

#VALIDATION LOCATORS
    EXISTING_EMAIL_INPUT_VALIDATION = (By.XPATH, "//label[text()='Email']/following-sibling::div/div")
    UNCHECKED_AGREE_TERMS_VALIDATION = (By.XPATH, "//label[contains(text(),'agree with')]/following-sibling::div")
