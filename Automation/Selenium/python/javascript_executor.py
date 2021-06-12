# https://dzone.com/articles/perform-actions-using-javascript-in-python-seleniu

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
javaScript = "alert('hello');"
driver.execute_script(javaScript)
driver.switch_to.alert.dismiss()
time.sleep(5)

driver.quit()

