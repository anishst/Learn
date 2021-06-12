from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://jqueryui.com/draggable/')

# drag test
driver.switch_to.frame(0)
source1 = driver.find_element_by_id('draggable')
action = ActionChains(driver)
# move element by x,y coordinates on the screen
action.drag_and_drop_by_offset(source1, 100, 100).perform()
time.sleep(5)

# drag and drop test
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(0)
source = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
time.sleep(5)

driver.quit()