# Electron practice app

https://www.electronjs.org/

any changes made on electron side requires app reload

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

## Video tools

- https://ffmpeg.org/download.html
- https://www.gyan.dev/ffmpeg/builds/
- https://windowsloop.com/install-ffmpeg-windows-10/#download-ffmpeg
- https://github.com/fluent-ffmpeg/node-fluent-ffmpeg
- https://www.npmjs.com/package/fluent-ffmpeg
  - npm install --save fluent-ffmpeg

  API Docs: https://www.electronjs.org/docs/api
## Security

https://github.com/electron/electron/blob/master/docs/tutorial/security.md

## Troubleshooting

Error: Electron Security Warning (Insecure Content-Security-Policy) This renderer process has either no Content Security
    Policy set or a policy with "unsafe-eval" enabled. This exposes users of
    this app to unnecessary security risks.

Fix: add this to header
```<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline';" />```


https://stackoverflow.com/questions/19059580/client-on-node-uncaught-referenceerror-require-is-not-defined