# Protractor
Protractor is an end-to-end test framework for Angular and AngularJS applications. 
Protractor runs tests against your application running in a real browser, interacting with it as a user would.

- Main: https://www.protractortest.org/#/tutorial
- Docs: https://www.protractortest.org/#/toc


Setup
==============================================================
1. Install Node
2. Install protractor globally: ```npm install -g protractor```
3. Install webdriver-manager helper tool to easily get an instance of a Selenium Server running: ```webdriver-manager update```
4. Start the server:``` webdriver-manager start```
5. Protractor needs two files to run, a spec file and a configuration file.
Example:
```
    // spec.js
    describe('Protractor Demo App', function() {
    it('should have a title', function() {
        browser.get('http://juliemr.github.io/protractor-demo/');

        expect(browser.getTitle()).toEqual('Super Calculator');
    });
    });
    // conf.js
    exports.config = {
    framework: 'jasmine',
    seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['spec.js']
    }
```
6. Run the script: ```protractor conf.js```


