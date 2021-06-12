from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True
driver = webdriver.Ie(capabilities=caps)
driver.implicitly_wait(10)
driver.get("http://localhost/index.html")

# find all paras within div tags
elm = driver.find_elements_by_css_selector("div > p")
for i in elm:
	print (i.text)


driver.quit()


