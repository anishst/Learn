# Webdriver IO

WebdriverIO is Javascript based test automation framework built over nodeJs. It is an open-source project developed for the automation testing community. 

https://webdriver.io/

##  Setup a test project

 Get started: https://webdriver.io/docs/gettingstarted.html
 ### Steps
1. initialize NPM project: 
    - mkdir webdriverio-test && cd webdriverio-test
    - npm init -y
2. Install WebdriverIO CLI - test runner
    - npm i --save-dev @wdio/cli
3. Generate config file  for executing Selenium scripts through WebdriverIO: ```./node_modules/.bin/wdio config -y```
4. Create spec files
    - create new folder: mkdir -p ./test/specs
    - basic.js
  
 ```const assert = require('assert')

describe('webdriver.io page', () => {
    it('should have the right title', async () => {
        await browser.url('https://webdriver.io')
        const title = await browser.getTitle()
        assert.strictEqual(title, 'WebdriverIO · Next-gen WebDriver test framework for Node.js')
    })
})
```
5. Run test: ```./node_modules/.bin/wdio wdio.conf.js```
## Resources

- Example blog post: https://www.lambdatest.com/blog/webdriverio-tutorial-with-examples-for-selenium-testing/
