import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# TODO: TEST CONFTEST
chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)

def test_chrome_test1():
	print("testing chrome using Docker image")
	chrome.get('https://www.google.com')
	time.sleep(5)
	print(chrome.title)

def test_chrome_test2():
	print("testing chrome using Docker image")
	chrome.get('https://www.google.com')
	time.sleep(5)
	print(chrome.title)

