from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

# see videos 175

class TestStatus(SeleniumDriver):

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):

        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(" ### VERIFICATION PASSED :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error(" ### VERIFICATION FAILED :: " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error(" ### VERIFICATION FAILED :: " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error(" ### EXCEPTION OCCURED! ")

    def mark(self, result, resultMessage):
        """Mark the result of the verification point in a test case"""
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verfication point a test case
        This needs to be called at least once in a test case
        This should be the final test status of the test case
        :param testName:
        :param result:
        :param resultMessage:
        :return:
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:

            self.log.error(testName + " ## TEST FAILED")
            self.resultList.clear()
            assert  True == False
        else:
            self.log.error(testName + " ### TEST PASSED ")
            self.resultList.clear()
            assert True == True
            
