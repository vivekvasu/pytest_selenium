import pytest
from selenium import webdriver
from src.main.configs.config import Config

from src.main.utils.file_reader import File_Reader

@pytest.fixture(scope='session')
def setup(request):
    path = '/Users/vivekvasu/vscode/pytest_selenium/config.json'
    config_data = File_Reader().read_json(path)
    config = Config.from_dict(config_data)
    driver = webdriver.Chrome()
    driver.get(config.url)
    request.session.test_config = config
    request.session.driver = driver
    yield
    driver.quit()
