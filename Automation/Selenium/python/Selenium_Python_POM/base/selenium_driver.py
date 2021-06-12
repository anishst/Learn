from selenium.webdriver.common.by import  By
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


#  Global variables
TIME_OUT = 15 # Number of seconds to wait for locating items before Timing out


class SeleniumDriver():

	# setup logging
	log = cl.custom_logger(logging.DEBUG)

	def __init__(self, driver):
		self.driver = driver


	def getTitle(self):
		return self.driver.title

	def getByType(self, locatorType):

		locatorType = locatorType.lower()

		if locatorType == 'id':
			return By.ID
		elif locatorType == 'name':
			return By.NAME
		elif locatorType == 'xpath':
			return By.XPATH
		elif locatorType == 'css':
			return By.CSS_SELECTOR
		elif locatorType == 'classname':
			return By.CLASS_NAME
		elif locatorType == 'link':
			return By.LINK_TEXT
		elif locatorType == 'partiallink':
			return By.PARTIAL_LINK_TEXT
		else:
			# print("Locator Type " + locatorType + " not correct/supported")
			self.log.info("Locator Type " + locatorType + " not correct/supported")


	def getElement(self, locator, locatorType='id'):
		"""
		this function will return the element using locator and locatorType
		:param locator:
		:param locatorType:
		:return:element
		"""

		element = None

		try:
			locatorType = locatorType.lower()
			byType = self.getByType(locatorType)
			element = WebDriverWait(self.driver, TIME_OUT).until(EC.element_to_be_clickable((byType, locator)))
			# element = self.driver.find_element(byType, locator)
			# print(f"Element found with locatior {locator}")
			self.log.info(f"Element found with locator: {locator}")
		except Exception as e:
			# print(f"Element was not found with locatior: {locator}")
			self.log.error(f"Element was not found with locator: {locator}. Exception: {e}")

		return element

	def elementClick(self, locator, locatorType='id'):
		"""
		This fucntion clicks on the element using locator and locatorytype values
		:param locator:
		:param locatorType:
		:return:
		"""
		try:
			element = self.getElement(locator, locatorType)
			element.click()
			# print(f"Clicked on element with locator: {locator} and locatorType: {locatorType}")
			self.log.info(f"Clicked on element with locator: {locator} and locatorType: {locatorType}")
		except Exception as e:
			# print(f"Cannot click on element with locator: {locator} and locatorType: {locatorType}")
			self.log.error(f"Cannot click on element with locator: {locator} and locatorType: {locatorType}. Exception: {e}")

			# print_stack()

	def sendKeys(self, data, locator, locatorType='id'):
		"""this function will send data to a field using  locator and locatoryType values

		data = what you want to type in the field

		locator = name/id for the field

		locatorType = how you want to locate the field
		"""
		try:
			element = self.getElement(locator, locatorType)
			element.send_keys(data)
			# print("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
			self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
		except Exception as e:
			# print("Cannot send data on element with " + locator + " locatorType: " + locatorType + str(e))
			self.log.error("Cannot send data on element with " + locator + " locatorType: " + locatorType + str(e))
			# print_stack()

	def isElementPresent(self, locator, byType):
		try:
			element = self.driver.find_element(byType, locator)
			if element is not None:
				print("Element found")
				return True
			else:
				print("Element not found")
				return False
		except:
			print("Element not found")

	def waitForElement(self, locator, locatorType='id', timeout=TIME_OUT, pollFrequency=0.5):
		element = None
		try:
			byType = self.getByType(locatorType)
			print("Waiting for a maximum :: " + str(timeout) +
				" :: seconds for element to be clickable")
			wait = WebDriverWait(self.driver, TIME_OUT, poll_frequency=1,
									ignored_exceptions=[NoSuchElementException,
														ElementNotVisibleException,
														ElementNotSelectableException])
			element = wait.until(EC.element_to_be_clickable((byType,
														locator)))

			
			print("Element appeared on the web page")
		except:
			print("Element did not appear on the web page!")
			# print_stack()
		return element


	def take_screenshot(self, resultMessage):

		"""
		This functions takes a screenshot of the current open page
		:return:
		"""

		# fileName = f"{resultMessage}.{str(round(time.time() * 1000))}.png"
		fileName = f"{self.driver.name}_{resultMessage}.{time.strftime('%m%d%Y%H%M%S')}.png"
		screenShotDirectory = "../screenshots/"
		relativeFileName = screenShotDirectory + fileName
		currentDirectory = os.path.dirname(__file__) # gives the file directory
		destinationFile = os.path.join(currentDirectory, relativeFileName)
		destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)
		try:
			# if screenshot folder doesn't exist, create it
			if not os.path.exists(destinationDirectory):
				print(f"{destinationDirectory} was not found. Creating....")
				os.makedirs(destinationDirectory)
			self.driver.save_screenshot(destinationFile)
			self.log.info(f"Screenshot saved to directory: {destinationFile}")
		except Exception as e:
			self.log.error(f"An exception occured while trying to save screenshot: {e}")
			print_stack()








