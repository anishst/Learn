# https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains	

driver = webdriver.Chrome()
driver.get("https://www.google.com")

actions = ActionChains(driver)
actions.send_keys("test")
actions.send_keys('hello')
actions.send_keys(Keys.SPACE)
actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

# action_chains = ActionChains(self.driver)
# action_chains.key_down(Keys.CONTROL).send_keys("a")
# action_chains.send_keys(Keys.DELETE)
# action_chains.send_keys("23.00")
# action_chains.send_keys(Keys.TAB)
# action_chains.send_keys('123456789')
# action_chains.perform()