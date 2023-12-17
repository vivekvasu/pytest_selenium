from selenium import webdriver

class DriverUtils:

    def __init__(self, driver) -> None:
        self.driver: webdriver  = driver

    def open_url(self, url: str):
        self.driver.get(url)
