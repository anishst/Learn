const electron = require('electron');

const { app, BrowserWindow } = electron;

app.on('ready', () => {
    // open a new browser window
    const mainWindow = new BrowserWindow({});
    // load local html page
    mainWindow.loadURL(`file://${__dirname}/index.html`)
    // navigate to google
    // mainWindow.loadURL('http://www.google.com')

    console.log("app is now ready");
});

