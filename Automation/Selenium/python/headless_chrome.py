from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()  
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(chrome_options=chrome_options)

print("Navigating to google.com...")
driver.get("http://www.google.com") 
search_field = driver.find_element_by_name("q")  
print("Searching for Cheese...")
search_field.send_keys("Cheese")  
search_field.send_keys(Keys.RETURN)  
assert "Cheese" in driver.page_source   
print(driver.page_source)
print("Search Complete!")
driver.close()
print("Script Complete!")