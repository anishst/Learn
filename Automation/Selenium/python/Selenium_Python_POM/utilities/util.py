import time
import random, string
import utilities.custom_logger as cl
import logging
import traceback

class Util(object):

    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """

        if info is not None:
            self.log.info(f"Waiting {sec} seconds for {info}" )
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        :param length: length of string
        :param type: type of characters
        :return:
        """

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters

        return alpha_num.join(random.choice(case) for i in range(length))


    def getUniqueName(self, charCount=10):
        """
        get a unique name
        :param charCount:
        :return:
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        get a list of unique names
        :param listSize: number of names needed
        :param itemLength: determin the length of each item in list > [1,2]; should be equal to the listsize
        :return:
        """
        namelist = []
        for i in range(0, listSize):
            namelist.append(self.getUniqueName(itemLength[i]))
        return namelist

    def getUniqueDigits(self, charCount=10):
        """
        get a unique name
        :param charCount:
        :return:
        """
        return self.getAlphaNumeric(charCount, 'digits')


    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualText:
        :param expectedText:
        :return: True/False
        """

        self.log.info(f"Actual Text from Application {actualText}")
        self.log.info(f"Expected text from application {expectedText}")
        if expectedText.lower() in actualText.lower():
            self.log.info(" ### TEXT MATCHES !!! ")
            return True
        else:
            self.log.error("### TEXT DOES NOT MATCH!!! ")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify actual text matches expected text string
        :param actualText:
        :param expectedText:
        :return: True/False
        """

        self.log.info(f"Actual Text from Application {actualText}")
        self.log.info(f"Expected text from application {expectedText}")
        if expectedText.lower() == actualText.lower():
            self.log.info(" ### TEXT MATCHES !!! ")
            return True
        else:
            self.log.error("### TEXT DOES NOT MATCH!!! ")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify 2 lists match
        :param expectedList:
        :param actualList:
        :return:
        """
        return set(expectedList) == set(actualList)


    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list
        :param expectedList:
        :param actualList:
        :return:
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True


