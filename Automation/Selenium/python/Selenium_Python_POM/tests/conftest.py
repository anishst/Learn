import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def driver(request):
    """
    this function yields a driver instance to be used in pytests.
    :param request:
    :return:
    """

    testURL = 'https://www.google.com'
    browserToUse = "Chrome" # Current supported Options are: "Chrome", "Ie", "Firefox"

    wdf = WebDriverFactory(browserToUse)
    driver = wdf.getWebDriverInstance(testURL)
    print("Getting Driver")
    print(f"running {request.function.__name__} ")
    yield driver
    print("Closing Driver")
    driver.quit()