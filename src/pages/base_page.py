from src.main.utils.driver_utils import DriverUtils


class BasePage(DriverUtils):

    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__(driver)
