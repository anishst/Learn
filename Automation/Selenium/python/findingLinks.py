from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

#  find links by tag name
elements = driver.find_elements_by_tag_name('a')
for element in elements:
	print(element.text)

#  find link by text
driver.find_element_by_link_text("Privacy").click()
time.sleep(3)
driver.back()
time.sleep(3)

#  find link by partial link text
driver.find_element_by_partial_link_text("Sto").click()
time.sleep(3)
driver.quit()