# Cypress

Test automation tool. all-in-one testing framework, assertion library, with mocking and stubbing.

- uses JavaScript
- NOT based on Selenium
- supports all major browsers
- [Features](https://www.cypress.io/features)
    - time travel - takes snapshots as you run
    - debuggable
    - automatic waiting
    - consistent results; fast
    - screenshots and videos
    - cross browser testing (locally and remote)
    - supports all types of testing
    
## Setup
- pre-reqs
    - Windows 7 and up
    - Linux ubuntu 12.04 and up
- [Install steps](https://docs.cypress.io/guides/getting-started/installing-cypress.html)
    - 2 ways
        - via Node JS (recommended)
        - direct download
- [API Commands]() https://docs.cypress.io/api/api/table-of-contents.html)

## Simple Test Project Setup

1. Go to project folder using command window
2. Initialize Project using default values: ```npm init -y ```
    - creates package.json file
3. Install Cypress:  
    - ```npm install cypress --save-dev```
    - specific version ```npm install cypress@<version#> --save-dev```
4. check cypress version: ```npx cypress -v```
5. Open cypress: ```npx cypress open``` 
    - this will open a window
    - you can close it for now
    - npx is a way to execute npm packages binaries
5. Cypress folder structure:
    ```
    ├───fixtures
    ├───integration - will store tests here
    │   └───examples - example test files; can be deleted
    ├───plugins - for plugins
    └───support
    ```


## Write 1st Test

1. write sample mocha script: first_test.js

    ```js
    // allow auto completion using cypress library
    /// <reference types="cypress" /> 

    // mocha test runner 
    it('google test', function () {

        cy.visit('https://www.google.com/');
    })
    ```
## Run tests

### Using Test Runner:
- run this command to bring up cypress window: ```npx cypress open```
- click your
 test script

### from command line in headless mode:  
- from root of app: ```npx cypress run```
- this also creates videos of run under: ```simple_test\cypress\videos```

### from command line in GUI mode:  
- with Chrome: ```npx cypress run --browser chrome```
- with Edge: ```npx cypress run --browser edge```
 - this also creates videos of run under: ```simple_test\cypress\videos```
### run from command line, specific test:
 ```npx cypress run --spec ./cypress/integration/first_test.js --browser edge```

[More Info on command Line Options](https://docs.cypress.io/guides/guides/command-line#Installation)
## [Element Interaction](https://docs.cypress.io/guides/core-concepts/interacting-with-elements)

See [API](https://docs.cypress.io/api/table-of-contents) for more info
- [Click()](https://docs.cypress.io/api/commands/click)
- Type()
- Clear()
- Check()
- Select()

## [Assertions](https://docs.cypress.io/guides/references/assertions#Chai)

- Cypress bundles the popular Chai assertion library
- [Implicit vs explicit waits](https://docs.cypress.io/guides/core-concepts/introduction-to-cypress#Writing-Assertions)
- [timeouts](https://docs.cypress.io/guides/core-concepts/introduction-to-cypress#Timeouts)

### [Hooks](https://docs.cypress.io/guides/core-concepts/writing-and-organizing-tests#Hooks)

- These are helpful to set conditions that you want to run before a set of tests or before each test. They're also helpful to clean up conditions after a set of tests or after each test.

### Fixtures and reading file types

- [Fixtures](https://docs.cypress.io/api/commands/route#Fixtures)
- using fixture to read file
    1. add userinfo.json file under *fixtures* folder
        ```json
        {
        "Username": "anish",
        "Password: "pass"
        }
        ```
    2. in the script read json as below: 
        ```javascript
        cy.fixture('userinfo').as('user')
        //use value from file to type in username TextBoxe
        cy.get('#UserName').type(user.Username)
       ```

## Screenshots
- to change default location, add below to cypress.json file:
    ```"screenshotsFolder": "cypress/videos"``` 
## Plugins        

-   [directory](https://docs.cypress.io/plugins/directory)
- installing

## Cucumber with Cypress

1. install [plugin](https://github.com/TheBrainFamily/cypress-cucumber-preprocessor ): ```npm install --save-dev cypress-cucumber-preprocessor```
2. add below to *plugins/index.js* file:
    ```javascript
    const cucumber = require('cypress-cucumber-preprocessor').default
    module.exports = (on, config) => {
    on('file:preprocessor', cucumber())
    }
    ```
3. (SKIP IF YOU HAVE OTHER TYPES OF TESTS) Add support for feature files to your Cypress configuration: cypress.json
    ```json
    {
        "testFiles": "**/*.feature"
    }
    ```
4. add this section to your package.json:
    ```json
        "cypress-cucumber-preprocessor": {
        "nonGlobalStepDefinitions": true
    }
    ```
5. Put your feature files in cypress/integration/
6. Run all feature tests: ```npx cypress run --spec **/*.feature```


## XHR and Cypress

**XMLHttpRequest (XHR)** objects are used to interact with servers. You can retrieve data from a URL without having to do a full page refresh. This enables a Web page to update just part of a page without disrupting what the user is doing. XMLHttpRequest is used heavily in AJAX programming. [more details](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

- support for XHR is built into cypress
- start server by : ```cy.server();```
- [stubbing XHR](https://www.cypress.io/blog/2019/09/05/cypress-code-coverage-for-create-react-app-v3/#stubbing-xhr)
- [getCookies](https://docs.cypress.io/api/commands/getcookies) - to read values of cookies

## API Testing with Cypress

- use [cy.request](https://docs.cypress.io/api/commands/request)
- you can use the [fake json server](https://github.com/typicode/json-server#getting-started)
    - install globally: ```npm install -g json-server```
    - add json db.json file in a folder and start json server from that directory: ```json-server --watch db.json```
    - Now if you go to http://localhost:3000/posts/1, you'll get: ```{ "id": 1, "title": "json-server", "author": "typicode" }```
- example test request
    ```javascript
        it("Test GET functionality of JSON Server", () => {
            cy.request("http://localhost:3000/posts/1").its('body').should('have.property', 'id');
        })
    ```    
## Dashboard 

The [Cypress Dashboard Service](https://www.cypress.io/dashboard/) is an optional web-based companion to the Test Runner.

- [pricing](https://www.cypress.io/pricing)

## Cypress Docker

- [Docker Images](https://docs.cypress.io/examples/examples/docker#Images)
- [Run Cypress with a single Docker command](https://www.cypress.io/blog/2019/05/02/run-cypress-with-a-single-docker-command/)
- [Docker Compose Example](https://github.com/cypress-io/cypress-example-docker-compose)

## Sample Codes

- hard wait for 4 second: ```cy.wait(4000)```
- timeout value: ```cy.get('.gLFyf', { timeout: 6000 }).type("Cypress{enter}");```
- use **cypress.json** to apply global options
    ```json
    {
        "watchForFileChanges": true,
        "defaultCommandTimeout": 5000
    }
    ```
    - [ more global options](https://docs.cypress.io/guides/references/configuration#Global) 

- table related
    - find all td : ```cy.get('.table').find('tr > td')```
    - find all td with my name : ```cy.get('.table').find('tr').contains('Anish')```
    - find all td with my name and click a link  : ```cy.get('.table').find('tr').contains('Anish').parent().contains('linkname').click()  ```
- [alias](https://docs.cypress.io/api/commands/as)
    -  ```
        cy.get('.table').find('tr').as("rows")
        cy.get("@rows").then($row) => {
            // click each row in table
            cy.wrap($row).click({multiple:true})
        }
        ```
- [wrap](https://docs.cypress.io/api/commands/wrap )
- [custom commands   ](https://docs.cypress.io/api/cypress-api/custom-commands)
  

## Notes: 

- Cypress gets installed under: C:\Users\ats\AppData\Local\Cypress\Cache\3.1.5\Cypress
- To remove cypress:  npm uninstall cypress

## Tools
- [Cucumber plugin for vscode](https://github.com/alexkrechik/VSCucumberAutoComplete)

## Resources
- [Cypress GitHub](https://github.com/cypress-io)
- [How to test for accessibility with Cypress](https://www.deque.com/blog/how-to-test-for-accessibility-with-cypress/)
- [Execute automation video series](https://bah.udemy.com/course/e2e-cypress)