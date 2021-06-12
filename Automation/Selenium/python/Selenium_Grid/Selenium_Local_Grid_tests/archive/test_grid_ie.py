from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


ie = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)

print("Testing ie using Grid")
ie.get('https://www.google.com')
print(ie.title)

ie.quit()
