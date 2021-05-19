# Testing

- [API Testing](#api_testing)
- [Performance Testing](#perf_testing)
## Levels of Testing
- **Unit testing** - verify your code at the level of functions and classes; positive and negative testing at the lowest layers of 
code; first safety net for catching bugs; should run fast; automate
- **Integration Testing** 
  - Component Testing - library and complied binary level tests - usually developers
  - system integration tests - testers
- **System Testing** - tests the external interfaces of a system which is a collection os sub-systems
- Performance Testing - testing done at sub-system and system levels to verify timing resource usages are acceptable
- **User Acceptance Testing** - is a level of software testing where a system is tested for acceptability. The purpose of this test is to evaluate the system's compliance with the business requirements and assess whether it is acceptable for delivery.
- alpha and beta Testing
- functional testing
  - functional testing; is it working? yes/no
- non-functional testing
  - usually measured as range
  - performance
  - load
  - usability
  - security
- black box testing
  - test without knowing internals
- white-box testing
  - testing while monitoring internal structure of system
- regression testing
- smoke testing/stability

# <a name="#perf_testing"></a>Performance Testing

- time takes to respond
- resource utilization
- capacity
- different types
  - load tests
    - focus on ability to handles increasing levels of loads by concurrent 
    users
    - Load profiles
      - operational profile
      - **ramp-ups**: steadily increasing load
      - **ramp_downs**: steadily decreasing load
      - steps: instantnouse changes in load(ex. add 100 virtual users every 5 mins)
      - predefined distributions(ex. volumes mimics daily or seasonal business cycles ; NIL, DIL)
  - stress tests
    - ability to handle peak loads; beyond limits
  - scalability tests
    - ability to meet future efficiency requirements
  - spike testig
    - bursts of load; sudden spikes; amazon prime day for example
  - endurance testing
    - stability of system overa long period
  - concurrency testing
    - same action by same users same time
  - capacity testing
    - how many users can use meeting requirements

## Tools
- Jmeter
  - [my notes](https://github.com/anishst/Learn/blob/master/Testing/Performance/jmeter_notes.md)
# BDD

Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. 

- extension of TDD
- tests are written first and then devlopment based on scenarios listed in tests
## Cucumber

Cucumber is a tool that supports Behaviour-Driven Development(BDD)

- https://cucumber.io/
- [step definitions](https://cucumber.io/docs/cucumber/step-definitions/)
 
```gherkin
Feature: Guess the word

  # The first example has two steps
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  # The second example has three steps
  Scenario: Breaker joins a game
    Given the Maker has started a game with the word "silky"
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```


# Agile Testing
Agile software development has resulted in burning down the silos of the traditional waterfall development methodology. 

Agile Manifesto:
- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

## Agile Metrics

- **Sprint velocity**: Velocity is the amount of work completed by the agile team in a given period of time. Sprint velocity is basically the rate at which the conditions mentioned in the software requirements specifications get converted into lines of tested code, or the number of story points covered by the team on every sprint.
- **Sprint burndown**: Also known as the burndown chart, this is a graphical representation of estimated tasks planned and the actual tasks completed. 


## Resources
- Getting Started - https://cucumber.io/guides/overview/#what-is-cucumber


## Gherkin

Gherkin is a simple set of grammar rules that makes plain text structured enough for Cucumber to understand.

Feautre file is composed of one feautre and multiple scenarios

- Gherkin Reference: https://cucumber.io/docs/gherkin/

### Syntax examples

GIVEN I am on the blog page\
WHEN I press the new post button\
THEN I am on the new post page

- Feature keyword - describes which part of the functionality scenarios are being created for.
- Scenario keyword - is used to describe the test case title.
- Given keyword - describes pre-conditions required to complete the scenario.
- When keyword - is used to describe the scenario’s steps.
- Then keyword - describes the expected result of the scenario.
- And keyword - can be used for Given, When and Then keywords to describe additional steps.


## Behave

**behave** is behaviour-driven development, Python style. Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. 

https://behave.readthedocs.io/en/latest/tutorial.html


```pip install behave```

###  Dev Info:

- all scenarios are kept in feature files that should be put in the features directory
- All scenario steps must have an implementation

Docs: https://behave.readthedocs.io/en/latest/
Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. 
### Test Driven Development (TDD) 
- practice of writing your test script before writing code

Workflow
 - red - write failing unit test
 - green - write passing unit test
 - refactor - clean up unit test

## 508 Compliance Testing

Section 508 requires that all website content be accessible to people with disabilities.

It is the law:
Section 508 of the Rehabilitation Act (29 U.S.C. 794d), as amended by the Workforce Investment Act of 1998 (P.L. 105-220), August 7, 1998.

Beginning January, 2018, new ADA regulations for web accessibility will go into effect. While organizations cannot be 100% compliant, there are steps that they can take to ensure their sites are accessible to those with disabilities.

### Some Checks to do:
- Review the Website Content Accessibility Guidelines (WCAG 2.0). These guidelines offer recommendations on how to make your website accessible; https://www.w3.org/WAI/standards-guidelines/wcag/
- Conduct an audit of your site using a WAVE Web Accessibility Tool. Google Chrome’s WAVE Tool is a great tool to look for accessible issues, including missing alt tags, styles, etc.; https://wave.webaim.org/
- Make sure your images have descriptive alt tags. Alt tags are used by screen readers, players, and voiceovers to describe elements on a website to users
- Keep inputs and forms accessible
- Enable keyboard navigation
- see this article for more tips: https://karlgroves.com/2018/05/25/automated-lies-with-one-line-of-code


# <a name="api_testing"></a>API Testing

API testing is a type of testing that involves verifying and validating APIs and Web services. Unlike traditional testing which focuses on functionality on the GUI interacted by end users, API testing checks APIs used by developers and occurs at the middle layer of the software (e.g., headless or GUI-less components, usually invisible to end-users).

# Web Services
Web service supports interoperable machine-to-machine interaction over a network

https://www.ibm.com/support/knowledgecenter/en/SSMKHH_9.0.0/com.ibm.etools.mft.doc/ac55710_.htm

### Free Web services for paractice
- http://www.dneonline.com/calculator.asmx?WSDL

## HTTP Verbs

- GET - retreive something; ex. GET item/1
- POST - rcvd data and use it; ex. POST/item
- PUT - make sure something is there; ex. PUT/item
- DELETE - remove something; ex. DELETE/item/1


# API Types

## SOAP
SOAP (Simple Object Access Protocol) is an XML message format used in Web service interactions
- WSDL is an XML notation for describing a web service
 - Latest version of SOAP is 1.2

https://www.tutorialspoint.com/soap/soap_quick_guide.htm


## REST

Representational state transfer (REST) is a software architectural style that defines a set of constraints to be used for creating Web services

### REST API

- returns a resource
- stateless; one request cannot depend on any other requests; server only knows about current request

## Videos
 - https://bah.udemy.com/course/rest-api-flask-and-python/learn/lecture/5993706#overview

## Git Repos
- https://github.com/schoolofcode-me/rest-api-sections


# API Test Tools

## SoapUI

SoapUI supports both REST and SOAP services. 

- to generate documenation: right click on webservice and use 'Generate Documentation'


### Tool Comparison
https://www.katalon.com/resources-center/blog/soapui-vs-postman-katalon-api-tools/

# Postman

API Testing tool

Postman can be installed as a browser extension or a desktop application on Mac, Linux, and Windows

Login/Download: https://www.getpostman.com/

Sample Request APIs: https://reqres.in/

### Shortcuts

```CTRL + ALT + C``` bring up console window
### Guides:
- Learning Center: https://learning.getpostman.com/
- Authorizing Requests:https://learning.getpostman.com/docs/postman/sending-api-requests/authorization/
- Adding Certificates: https://learning.getpostman.com/docs/postman/sending-api-requests/certificates/
- Soap Requests: https://blog.getpostman.com/2017/11/18/postman-makes-soap-requests-too/
- Certs: https://learning.getpostman.com/docs/postman/sending-api-requests/certificates/

### Collections
Group of API requests

Variables can be created at Collection/Env levels
- using variables: {{url}}/api/users/2
- scope levels: collection; env; global
Test Example:
```
console.log("Hello World!")
// get variable
let urlVar = pm.variables.get("url")
console.log("Value for URL variable is: " + urlVar)
// set variable
pm.variables.set("NAME", 'postman')
console.log(pm.variables.get("NAME"))
```

### Environments

- allows to switch between environments; ex. url
- local vs global
- https://learning.postman.com/docs/postman/variables-and-environments/variables/


use SNIPPETS to save time

### Chrome Extensions

- **Wizdler** Parses the WSDL files and generates SOAP messages for you.
https://chrome.google.com/webstore/detail/wizdler/oebpmncolmhiapingjaagmapififiakb?hl=en

### Running from command line

- use newman to run postman request from command line: https://www.npmjs.com/package/newman
- install newman globally; need node installed: ```npm install -g newman```
- To run: ```newman run <collections.json>```
- to run with specific enviornment:
    - download env var json file; make sure initial value is populated
    - then run ```newman run -e <envfile.json> <collections.json>```
 - use -n option to run multiple times; see doc: https://learning.postman.com/docs/postman/collection-runs/command-line-integration-with-newman/#options
 
- html reports
    - docs:  https://www.npmjs.com/package/newman#html-reporter
    - ```npm install -g newman-reporter-html```
    - demo: https://www.youtube.com/watch?v=uNUi_Sg57kM
    - demo: advanced html: https://www.youtube.com/watch?v=CBzJeK-MH6Y

### Integration with Jenkins
- https://learning.postman.com/docs/running-collections/using-newman-cli/integration-with-jenkins/
- demo: https://www.youtube.com/watch?v=93FRB1LdRAA

### workflows

- https://learning.postman.com/docs/postman/collection-runs/building-workflows/

### Debugging

- https://learning.postman.com/docs/postman/sending-api-requests/debugging-and-logs/
- use console to monitor and log
- pre-requisites tab example:
```javascript
var name = "Anish Postman"
console.log("name is " + name)
console.info("info for " + name)
console.warn("warning for " + name)
console.error("error for " + name)
// set a global var
pm.globals.set("test",name);
console.log("Global var is " + pm.globals.get("test"));
```
- pre-requistes can be at individual request level or collection level: https://learning.postman.com/docs/postman/scripts/pre-request-scripts/

### Using Curl

- click Import
- enter url ```curl --location --request GET 'https://postman-echo.com/get?foo1=bar1&foo2=bar2```
- examples: https://docs.postman-echo.com/?version=latest#intro

### Getting XML value from XML response

Response:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/" xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
    <env:Header/>
    <S:Body>
        <OpenSessionResponse xmlns="<url>" xmlns:ns2="<nsurl>">
            <SessionHeader>
                <SessionID>60851343195</SessionID>
            </SessionHeader>
        </OpenSessionResponse>
    </S:Body>
</S:Envelope>
```
Getting sessionid from response using Javascript:   
```javascript
// convert xml response to JSON format
var responseJson = xml2Json(responseBody);
// print entire response
console.log(responseJson);
// print session id
console.log(responseJson["S:Envelope"]["S:Body"]["OpenSessionResponse"]["SessionHeader"]["SessionID"]);```
// set global variable
pm.globals.set("SessionID", responseJson["S:Envelope"]["S:Body"]["OpenSessionResponse"]["SessionHeader"]["SessionID"])
console.log(pm.globals.get("SessionID"));
```
### Data Driven Testing

Use data files to run requests using a file

https://learning.postman.com/docs/running-collections/working-with-data-files/


request forrmat:
```json
{
    "email": "{{email}}",
    "password": "{{password}}"
}
```
CSV data input format:
```csv
endpoint,email,password
api/register/preprod,tes@yahh,hell
api/register/preprod,sf@yah,hell
```

JSON data input Format:
```json
[
	{
		"endpoint": "api/register/preprod",
		"email": "te@yaho",
		"password": "password"
	},
	{
		"endpoint": "api/register/preprod",
		"email": "maine@yaho",
		"password": "password"
	}
]

```
code to access variable in tests:

```javascript
// only works when using data file to run
tests["Contains email"] = responseBody.has(data.email);
tests["Contains password"] = responseBody.has(data["password"]);
```
### Tool Comparison
https://www.katalon.com/resources-center/blog/soapui-vs-postman-katalon-api-tools/

### Checklists
- WebAIM Checklist: https://webaim.org/standards/wcag/checklist
- ADA Checklist: https://www.ada.gov/pcatoolkit/chap5chklist.htm
- How to Meet WCAG: https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0
- https://a11yproject.com/checklist/

### Mobile Accessiblity

-  https://www.w3.org/WAI/standards-guidelines/mobile/
- https://interactiveaccessibility.com/blog/mobile-accessibility-move#.Xle-V6hKiUk
## Blogs

- https://karlgroves.com/category/accessibility-testing


## Tools

### Automation
- Selenium
- UFTOne
- Katalon
- [Ghost inspector](https://ghostinspector.com/)
- MicroFocus storm runner
- NuSum
### Performance
- JMeter
- Gatling
### TestComplete
- record and playback options
- has JIRA and Jenkins integration
- support coding using 7? different programming lanugages; ex. Python
- supports both desktop and web applications

# Blogs
- https://www.automatetheplanet.com/
- https://willowtreeapps.com/ideas
- Google Testing: https://testing.googleblog.com/
- https://testguild.com/blog/
- https://www.rainforestqa.com/blog/