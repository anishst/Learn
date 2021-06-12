from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://jqueryui.com/draggable/')

elm = driver.find_element_by_xpath('//*[@id="logo-events"]/h2/a')
action = ActionChains(driver)
action.context_click(elm).perform()
time.sleep(5)



driver.quit()