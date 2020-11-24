# Node JS

Node.js is an open-source server side runtime environment built on Chrome's V8 JavaScript engine. It provides an event driven, non-blocking (asynchronous) I/O and cross-platform runtime environment for building highly scalable server-side applications using JavaScript.

- Info: https://nodejs.org/en/about/

- API Info: https://nodejs.org/dist/latest-v14.x/docs/api/

## Node Web Frameworks

### express

- https://expressjs.com/
- Getting started guide: https://expressjs.com/en/starter/installing.html
- API https://expressjs.com/en/4x/api.html

## Setting up an express project

1. create project folder
2. run ```npm init --yes```
3. install express: ```npm i express```

### Express notes
- by default only servers files in root and views folder
-  create a public directory
    - ```app.use(express.static('public'))```
- routing : https://expressjs.com/en/guide/routing.html 
    - allows chaining routes

## Node Commands

Command | Description
-------| -------------
```npm i <packagename>``` | installs packages
```npm install <packagename>``` | installs packages
```npm update <packagename>``` | updates package
```npm install -g <packagename>``` | installs packages globally
```npm uninstall <packagename>``` | uninstalls package


## Node Packages

- global packages are installed under: ```%USERPROFILE%\AppData\Roaming\npm\node_modules```

### nodemon 
nodemon is a tool that helps develop node.js based applications by automatically restarting the node application when file changes in the directory are detected

https://www.npmjs.com/package/nodemon

install globally: ```npm i -g nodemon

install locally: ```npm i nodemon

to run app using nodemon: ```nodemon <appname>```
- use ```rs``` command to restart manually if needed

## Databases

###  MongoDB
- Native driver
    - https://docs.mongodb.com/drivers/node/quick-started
- Mongoose - ODM
    - preferred way
    - https://mongoosejs.com/
    - example: 
        ```
        const mongoose = require('mongoose');
        mongoose.connect('mongodb://localhost:27017/test', {useNewUrlParser: true, useUnifiedTopology: true});

        const Cat = mongoose.model('Cat', { name: String });

        const kitty = new Cat({ name: 'Zildjian' });
        kitty.save().then(() => console.log('meow'));
        ```
    - Schema validation allows you check the data being inserted into the database -  https://mongoosejs.com/docs/validation.html
    - Subdocuments/Embedded Documents - Embedded documents are documents with schemas of their own that are part of other documents (as items within an array).https://mongoosejs.com/docs/subdocs.html

## Templating

https://ejs.co/


## Deployement

- Using Heroku - https://devcenter.heroku.com/articles/deploying-nodejs
    - guide: https://bah.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/12386014#overview

## Tutorials
- https://www.tutorialsteacher.com/nodejs/nodejs-tutorials
- https://www.appbrewery.co/p/web-development-course-resources