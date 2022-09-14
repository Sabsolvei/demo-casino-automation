class BaseStep:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element, arg):
        self.driver.execute_script(arg, element)
