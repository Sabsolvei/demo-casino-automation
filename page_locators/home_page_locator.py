from selenium.webdriver.common.by import By


class HomePageLocator(object):
    SIGNUP_BUTTON = (By.XPATH, "//a[@href='/user/registration']")
    GOTIT_BUTTON = (By.XPATH, "//button/span[text()='Got it']")
