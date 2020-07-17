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
