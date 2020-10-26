const electron = require('electron');

const { app, BrowserWindow, Menu } = electron;

// global window var
let mainWindow;

app.on('ready', () => {
    // open a new browser window
    mainWindow = new BrowserWindow({ webPreferences: { nodeIntegration: true } });
    // load main page
    mainWindow.loadURL(`file://${__dirname}/main.html`);

    // setup custom menu
    const mainMenu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(mainMenu);
});


// menu template
// each object in array represents a menu item ; ex. File
// accelerator = for keyboard shortcuts
const menuTemplate = [
    {
        label: 'File',
        submenu: [
            {
                label: 'New To Do'
            },
            {
                label: 'Quit',
                accelerator: (() => {
                    if (process.platform === 'darwin') {
                        return 'Command+Q';
                    } else {
                        return 'Ctrl+Q';
                    }
                })(),
                click() {
                    app.quit();
                }
            }
        ]
    },
    {
        label: 'Help'
    }
];

// check os name and empty menu if Mac OS
if (process.platform === 'darwin') {
    menuTemplate.unshift({});
}