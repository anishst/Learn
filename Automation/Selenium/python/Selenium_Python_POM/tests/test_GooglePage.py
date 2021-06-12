from pages.google_page import GoogleSearch
import pytest

# to do mark skip if cetain users
@pytest.mark.usefixtures(scope="module")
class TestGoogle():

    def test_SearchForCheese(self, driver):
        googlePageTest = GoogleSearch(driver)
        assert googlePageTest.verifyGooglePageTitle()
        googlePageTest.googleSearch("Cheese")
        googlePageTest.take_screenshot("Test")

    def test_SearchForPython(self, driver):
        googlePageTest = GoogleSearch(driver)
        assert googlePageTest.verifyGooglePageTitle()
        googlePageTest.googleSearch("Python")
        googlePageTest.take_screenshot("Test")