import pytest

#  to test run from command line: pytest test_take_screenshot_on_failure.py --html=reports\test.html
def test_screenshot_on_test_failure(browser):
    browser.get("https://google.com")
    assert False