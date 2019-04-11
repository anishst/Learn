
# Mocha
unit testing framework for JavaScript
- Main page: https://mochajs.org/
- Getting started: https://mochajs.org/#getting-started
# Chai
JavaScript assertion library
- https://www.chaijs.com/
## Setup
- make sure node js is installed
- create a test folder
- run command on the folder to initialize: ```npm init -y```
- download mocha by using cmd: ```npm install --save-dev mocha```
- download chai by using cmd: ```npm install --save-dev chai``` 
- creata test.js file
```var assert = require('assert');
describe('Array', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
      assert.equal([1, 2, 3].indexOf(4), -1);
    });
  });
});
```
- run in command prompt ```node ./node_modules/mocha/bin/mocha```
- shows results
```
  Array
    #indexOf()
      √ should return -1 when the value is not present


  1 passing (0ms)
  ```

