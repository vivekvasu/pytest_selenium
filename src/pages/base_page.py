class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def enter_text(self, element, text):
        element.send_keys(str(text))
