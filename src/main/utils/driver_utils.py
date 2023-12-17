from selenium import webdriver

class DriverUtils:

    def __init__(self, driver) -> None:
        self.driver: webdriver  = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def enter_text(self, element, text):
        element.send_keys(str(text))

    def quit_driver(self):
        self.driver.quit()
