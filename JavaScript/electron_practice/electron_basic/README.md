# Electron practice app

1. create node package: ```npm init```
2. install electron: ```npm install --save electron```
3. create index.js file

    ```javascript
    const electron = require('electron');
    
    const { app } = electron;
    
    app.on('ready', () => {
        console.log("app is now ready");
    });
    ```

4. edit package.json: 
    ```json
      "scripts": {
        "electron": "electron ."
      }
    ```

5. run app by: ```npm run electron```