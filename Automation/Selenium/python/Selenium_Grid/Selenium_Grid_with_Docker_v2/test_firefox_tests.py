from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


firefox = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX) 



def test_fftest1():	
	print("Testing firefox using Docker Image")
	firefox.get('https://www.google.com')
	print(firefox.title)


def test_fftest2():	
	print("Testing firefox using Docker Image")
	firefox.get('https://www.google.com')
	print(firefox.title)

# chrome.quit()
# firefox.quit()