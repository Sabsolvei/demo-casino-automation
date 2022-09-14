from selenium.webdriver.common.by import By


class ConfirmEmailPageLocator(object):

    CODE_INPUT = (By.XPATH, "//label[text()='Verification code']/following-sibling::div/input")
    REQUEST_CODE_BUTTON = (By.XPATH, "//button/span[contains(text(),'Request code')]")
    VERIFY_BUTTON = (By.XPATH, "//button/span[contains(text(),'Verify')]")
    TITLE = (By.XPATH, "//h1[@class='notification__title']")
    DESCRIPTION = (By.XPATH, "//p[@class='notification__description']")


