# API Testing

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


## Postman

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
 
### workflows

- https://learning.postman.com/docs/postman/collection-runs/building-workflows/

### Debugging

- https://learning.postman.com/docs/postman/sending-api-requests/debugging-and-logs/
- use console to monitor and log

### Tool Comparison
https://www.katalon.com/resources-center/blog/soapui-vs-postman-katalon-api-tools/
