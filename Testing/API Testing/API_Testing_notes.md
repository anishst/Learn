# API Testing

API testing is a type of testing that involves verifying and validating APIs and Web services. Unlike traditional testing which focuses on functionality on the GUI interacted by end users, API testing checks APIs used by developers and occurs at the middle layer of the software (e.g., headless or GUI-less components, usually invisible to end-users).

# Web Services
Web service supports interoperable machine-to-machine interaction over a network

https://www.ibm.com/support/knowledgecenter/en/SSMKHH_9.0.0/com.ibm.etools.mft.doc/ac55710_.htm

### Free Web services for paractice
- http://www.dneonline.com/calculator.asmx?WSDL

## API Types

### SOAP
SOAP (Simple Object Access Protocol) is an XML message format used in Web service interactions
- WSDL is an XML notation for describing a web service
 - Latest version of SOAP is 1.2

https://www.tutorialspoint.com/soap/soap_quick_guide.htm


### REST


# API Test Tools

## SoapUI

SoapUI supports both REST and SOAP services. 


## Postman
Postman can be installed as a browser extension or a desktop application on Mac, Linux, and Windows

Login/Download: https://www.getpostman.com/

Sample Request APIs: https://reqres.in/

### Collections
Group of API requests

Variables can be created at Collection/Env levels

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
use SNIPPETS to save time


### Tool Comparison
https://www.katalon.com/resources-center/blog/soapui-vs-postman-katalon-api-tools/
