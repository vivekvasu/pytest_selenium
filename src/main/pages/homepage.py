from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage

class Homepage(BasePage):

    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__(driver)

    @property
    def search_input(self): return self.driver.find_element(by=By.NAME, value="q")


    def search(self, keyword: str):
        self.enter_text(self.search_input, keyword)
