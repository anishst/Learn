import utilities.custom_logger as cl
import logging
from base.basepage import BasePage



class GoogleSearch(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    # constructor
    def  __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators or page elements
    _search_field = 'q'
    _search_button = "btnK"

    # actions performed on the element

    def enterSearchData(self, searchvalue):
        self.sendKeys(searchvalue, self._search_field, locatorType="name")


    def clickSearchButton(self):
        self.elementClick(self._search_button, locatorType='name')

    # main actions - tests to be conducted

    def googleSearch(self, searchvlaue):
        self.enterSearchData(searchvlaue)
        self.clickSearchButton()

    def verifyGooglePageTitle(self):
        return self.verifyPageTitle("Google")
