from common.base_steps import BaseStep
from common.base_waits import BaseWait


class BaseStepWait(BaseWait, BaseStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
