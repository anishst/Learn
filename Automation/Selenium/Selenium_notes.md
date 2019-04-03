# Selenium

Selenium is a popular automation testing framework that is primarily used for cross browser testing. It is open source and is ideal for automating testing of web applications across different browsers like Firefox, Chrome, Internet Explorer, and Microsoft Edge.

## Components
- **Selenium Integrated Development Environment (IDE)** - simple browser plugin and it is used to record and playback scripts. ; firefox and chrome only
- **Selenium Remote Control (RC)** - Selenium RC is a standalone Java program that will allow you to execute HTML test suites; based on the client-server model which makes it possible to execute tests on the browser that is controlled by the server.
- **Selenium webdriver** - Selenium WebDriver framework is implemented through a browser-specific driver e.g. each browser will have its corresponding WebDriver application on which the automation testing would be performed; Selenium WebDriver directly communicates with the browser, so it does not require any separate component like the Selenium Server.
- **Selenium Grid** - Selenium Grid is mainly used for parallel testing since it helps run tests on different machines against different browsers & operating systems, simultaneously. It does the job in conjunction with Selenium RC.


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
- pytest

Java
- TestNG
- Junit/Nunit

## Page Object Model

Page Object model is an object design pattern in Selenium. Web pages are represented as classes, and elements on the page are defined as variables on the class, so user interactions can then be implemented as methods on the class.

Page Factory expands on Page Object model functionality by introducing more advanced features. It allows users to initialize specific elements within the Page Object model, using annotations.

- https://www.toptal.com/selenium/test-automation-in-selenium-using-page-object-model-and-page-factory


## WebDriverManager

WebDriverManager allows to automate the management of the binary drivers (e.g. chromedriver, geckodriver, etc.) required by Selenium WebDriver.

Java Version: https://github.com/bonigarcia/webdrivermanager

### Usage with Python
Python Version: https://github.com/SergeyPirogov/webdriver_manager

Install: ``` pip install webdriver_manager ```

### Guided Videos

### Guides
http://allselenium.info/browser-drivers-with-python-webdrivermanager/



