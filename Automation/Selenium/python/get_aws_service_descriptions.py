from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
import pytest


chrome_options = Options()
# chrome_options.add_argument("--window-size=1024,768")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(15)
driver.get("https://aws.amazon.com/products/")
items = driver.find_elements_by_xpath("//div[@class='lb-content-item']/a")


print(items)
for item in items:
    print(item.text)

driver.quit()

