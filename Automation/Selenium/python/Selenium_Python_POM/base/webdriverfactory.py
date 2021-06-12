"""
WebDriver Factory Class

Usage Example:
wdf = WebDriverFactory(browser)
wdf.getWebDriverInstance

# tuto 173
"""

from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits the WebDriverFactory class
        :param browser:
        """

        self.browser = browser

    def getWebDriverInstance(self, baseURL = 'https://www.google.com'):
        """

        :param baseURL: url of the website to test; default is google.com
        :return: instance of the requested web driver
        """


        if self.browser.lower() == "ff" or self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser.lower() == "ie":
            driver = webdriver.Ie()
        elif self.browser.lower() == "chrome":
            driver = webdriver.Chrome()

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
