const electron = require('electron');
const ffmpeg = require('fluent-ffmpeg');

const { app, BrowserWindow, ipcMain } = electron;

// global window var
let mainWindow;

app.on('ready', () => {
    // open a new browser window
    mainWindow = new BrowserWindow({
        // code to prevent 
        webPreferences: {
            nodeIntegration: true
        }

    });
    // load local html page
    mainWindow.loadURL(`file://${__dirname}/index.html`)
    // navigate to google
    // mainWindow.loadURL('http://www.google.com')
    console.log("app is now ready");
});

// arrow function to listen for video sumbit from index.html
ipcMain.on('video:submit', (event, path) => {

    // get video info
    ffmpeg.ffprobe(path, (err, metadata) => {
        // console.log('Video duration is: ', metadata.format.duration, 'seconds');
        // send details to mainwindow
        mainWindow.webContents.send('video:metadata', metadata.format.duration);
    });

});