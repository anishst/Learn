from selenium import webdriver

driver = webdriver.Ie()
driver.get('http://localhost:8080/otcnet/batchloader/TestClient.jsf')

ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    # print (ii.tag_name)
    print (ii.get_attribute('id'))   