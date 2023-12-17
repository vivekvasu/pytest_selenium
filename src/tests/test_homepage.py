import allure
import pytest

from src.pages.homepage import Homepage


@allure.parent_suite("Regression")
@allure.suite("Homepage Test")
@pytest.mark.usefixtures('setup')
class TestHomePage:

    @allure.description("Search for a keyword")
    def test_search(setup, request):
        driver = request.session.driver
        homepage = Homepage(driver)
        homepage.search("Test")
