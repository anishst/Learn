const electron = require('electron');

const { app, BrowserWindow, Menu, ipcMain } = electron;

// global window var
let mainWindow;
let addWindow;

app.on('ready', () => {
    // open a new browser window
    mainWindow = new BrowserWindow({ webPreferences: { nodeIntegration: true } });
    // load main page
    mainWindow.loadURL(`file://${__dirname}/main.html`);
    // event listner to close app and other windows opened by app
    mainWindow.on('closed', () => app.quit());

    // setup custom menu
    const mainMenu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(mainMenu);
});

// arrow function to listen for video sumbit from add.html
ipcMain.on('todo:add', (event, todo) => {

    mainWindow.webContents.send('todo:add', todo);
    // close add to do winodw
    addWindow.close();

});

function createAddWindow() {
    addWindow = new BrowserWindow({
        width: 300,
        height: 200,
        title: "Add New To Do",
        webPreferences: { nodeIntegration: true }
    });
    addWindow.loadURL(`file://${__dirname}/add.html`);
    // garabage collection
    addWindow.on('closed', () => addWindow = null);
};

// menu template
// each object in array represents a menu item ; ex. File
// accelerator = for keyboard shortcuts
const menuTemplate = [
    {
        label: 'File',
        submenu: [
            {
                label: 'Add To Do',
                click() {
                    createAddWindow();
                }
            },
            {
                label: 'Clear To Dos',
                click() {
                    mainWindow.webContents.send('todo:clear');
                }
            },
            {
                label: 'Quit',
                accelerator: process.platform === 'darwin' ? 'Command+Q' : 'Ctrl+Q',
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

// display developer tools if not prod version
if (process.env.NODE_ENV !== 'production') {
    menuTemplate.push({
        label: 'View',
        submenu: [
            { role: 'reload' },
            {
                label: 'Toggle Dev Tools',
                accelerator: process.platform === 'darwin' ? 'Command+Alt+I' : 'Ctrl+Shift+I',
                click(item, focusedWindow) {
                    focusedWindow.toggleDevTools();
                }
            }
        ]
    });
}