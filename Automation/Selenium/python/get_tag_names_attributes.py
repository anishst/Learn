from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com')

ids = driver.find_elements_by_xpath('//a')
for i in ids:
    print (i.tag_name)
    print (i.get_attribute('id'))
    print (i.get_attribute('value'))
    print (i.get_attribute('href'))
    print(i.get_attribute('innerHTML'))
