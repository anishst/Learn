# Selenium

Selenium is a popular automation testing framework that is primarily used for cross browser testing. It is open source and is ideal for automating testing of web applications across different browsers like Firefox, Chrome, Internet Explorer, and Microsoft Edge.

## Components
- **Selenium Integrated Development Environment (IDE)** - simple browser plugin and it is used to record and playback scripts. ; firefox and chrome only
- **Selenium Remote Control (RC)** - Selenium RC is a standalone Java program that will allow you to execute HTML test suites; based on the client-server model which makes it possible to execute tests on the browser that is controlled by the server.
- **Selenium webdriver** - Selenium WebDriver framework is implemented through a browser-specific driver e.g. each browser will have its corresponding WebDriver application on which the automation testing would be performed; Selenium WebDriver directly communicates with the browser, so it does not require any separate component like the Selenium Server.
- **Selenium Grid** - Selenium Grid is mainly used for parallel testing since it helps run tests on different machines against different browsers & operating systems, simultaneously. It does the job in conjunction with Selenium RC.

# Downloads

Releases: https://selenium-release.storage.googleapis.com/index.html

# Page Object Model

Page Object model is an object design pattern in Selenium. Web pages are represented as classes, and elements on the page are defined as variables on the class, so user interactions can then be implemented as methods on the class.

Page Factory expands on Page Object model functionality by introducing more advanced features. It allows users to initialize specific elements within the Page Object model, using annotations.


### Resources
- https://www.toptal.com/selenium/test-automation-in-selenium-using-page-object-model-and-page-factory
- https://github.com/SeleniumHQ/selenium/blob/master/py/test/selenium/webdriver/common/driver_element_finding_tests.py
- https://selenium-python.readthedocs.io/page-objects.html
- https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html
- http://www.seleniumframework.com/python-frameworks/implement-page-object-pattern/

## Locating Items

Locator | Description
------|------------
```driver.find_element_by_partial_link_text("Google").click()```| by link text
```driver.find_element_by_xpath("//input[@type='checkbox']").click()```| by xpath
```driver.find_element_by_css_selector("*[id^='pagebody:'][id$=':processName']"))```| by css selector

## Code Snippets

### Get all attribute values

```
inputs = driver.find_elements_by_xpath('//*[@id]')  
for i in inputs:
    print(i.get_attribute('id'))
```

### Use variables concat
```
value = EnvList[Env]
driver.find_element_by_xpath("//td[contains(text(), '" + value + "')]/preceding-sibling::td/div/input[@type='checkbox']")

```

### Handle TextBoxes

```
elm.send_keys(Keys.CONTROL + "a")
elm.send_keys(Keys.DELETE)
```

### Handle Frames

```
driver.switch_to_frame(driver.find_element_by_id("robIFrame"))
driver.switch_to_default_content()
```

### list all links on the page
```
elems = driver.find_elements_by_xpath("//*[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
    elem.click();
```

### check boxes
```
# select using xpath using mutliple attributes
CloseBatchChkBoxes = driver.find_elements_by_xpath("//input[@type='checkbox' and @alt='Start Up']")
    for checkbox in CloseBatchChkBoxes:
        checkbox.click()
```

### Radio buttons

```
radio = driver.find_elements_by_xpath("//*[@type='radio']")[1]
print(radio.is_selected())
driver.find_elements_by_xpath("//*[@type='radio']")[0].click()
```

### Tables

```
table = driver.find_element_by_xpath("//table[@class='entriesTable stripe']")
print(table.text)
rows = table.find_elements_by_xpath("//tbody/descendant::tr")
for row in rows:
    print(row.text)
```

### Dropdowns

```
from selenium.webdriver.common.by import By
....
ScannerTypeDD = Select(driver.find_element_by_id("pagebody:checkConfig:scannerMenu"))
ScannerTypeDD.select_by_visible_text(Scanner) 

# Print values of dropdown
processDD = Select(self.driver.find_element_by_id("pagebody:j_id_4r:processName"))

# for printing  values of displayed item
options = processDD.options
for element in options:
    print(element.get_attribute("value"))

# for printing  text displayed
options = AgencySiteDD.options
for element in options:
    print(element.get_attribute("text"))

# select by text
processDD.select_by_visible_text('CashlinkII TRS Extract Version 4.6')
# select by index
CCodeDD.select_by_index(1)

# Function select a text from dropdown
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
....
def select_by_text(web_element, select_text):
    """given a web element representing a select object, click the option 
    matching select_text
    """
    option_is_found = False
    options = web_element.find_elements_by_tag_name('option')
    for option in options:
        if option.text.strip() == select_text:
            option.click()
            option_is_found = True
            break
    if option_is_found == False:
        raise NoSuchElementException('could not find the requested element')
        
```

### Ignore certain values

```python
       drop_down_element = Select(deposit_test.get_element(By.ID, 'pagebody:defineDeposit:foreignCheckCurrencyCountry'))
        values_to_ignore = ['Select...', 'OTHER']
        while drop_down_element.first_selected_option.text in values_to_ignore:
            deposit_test.select_fcheck_country_code()
            drop_down_element = Select(deposit_test.get_element(By.ID, 'pagebody:defineDeposit:foreignCheckCurrencyCountry'))
            print(f"New selection: {drop_down_element.first_selected_option.text}")
```
## File upload
```
driver.find_element_by_id('batchLoader:checkImageFront').send_keys(r"C:\Users\username\Downloads\filename.tif")
```
##  Handling Waits


- Help: http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
```

# Example 1: using WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
...
LoginButtonXPath = "//input[@value='Log In']"
LoginButtonElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(LoginButtonXPath))
LoginButtonElement.click()

# Example 2 - with expected_conditions and WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
....
try:
    WebDriverWait(driver,10).until(EC.title_contains("cheese"))
    print(driver.title)
    link = driver
finally:
    driver.quit()
```


## Docs
Main Project Site: https://www.seleniumhq.org/docs/ 

## About articles
- https://www.sitepoint.com/how-to-use-selenium-webdriver-for-cross-browser-testing/?utm_campaign=1096170&utm_source=sendpulse&utm_medium=push
## Favorite Blogs
- http://allselenium.info/



## Test Frameworks

Test Frameworks befenfits:
- helps to manage tests
- test data
- generate reports
- logs

Python
- unittest
## Unit test example

```
from selenium   import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class DemoSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_SearchGoogle(self): 
        driver = self.driver
        driver.get("http://www.google.com")
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys("cheese")
        inputElement.submit()
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
```
- pytest

Java
- TestNG
- Junit/Nunit

## Reporting

Allure with pytest: https://docs.qameta.io/allure/#_pytest
## WebDriverManager

WebDriverManager allows to automate the management of the binary drivers (e.g. chromedriver, geckodriver, etc.) required by Selenium WebDriver.

Java Version: https://github.com/bonigarcia/webdrivermanager

### Usage with Python
Python Version: https://github.com/SergeyPirogov/webdriver_manager

Install: ``` pip install webdriver_manager ```

### Guided Videos

### Guides
- http://allselenium.info/browser-drivers-with-python-webdrivermanager/
- https://www.youtube.com/watch?v=5FUdrBq-WFo&t=5137s
- https://qxf2.com/blog/selenium-tutorial-for-beginners/

Driver factor example: https://github.com/qxf2/42Floors/blob/master/DriverFactory.py

## Known Issues

Issue:
Slow Typing with IE64-bit driver

Solution: 
1.Open IE
2.Go to Internet Options → Advanced → Security
3.Check ☑ Enable 64-bit processes for Enhanced Protected Mode
4. enable enhanced protected mode for all zones
https://stackoverflow.com/questions/27985300/selenium-webdriver-typing-very-slow-in-text-field-on-ie-browser