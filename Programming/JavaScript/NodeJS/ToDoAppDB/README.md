# Node JS To Do App

- To Do app using mongo db
    - app allows adding new todo lists on the fly
- make sure Mongo Sever is running on port: ```<ipaddress>:27017```; you may use docker
- ejs docs: https://ejs.co/#docs
- https://github.com/mde/ejs/wiki/Using-EJS-with-Express
- lodash docs: https://lodash.com/docs/2.4.2


1. create folder 
2. create files:  app.js, index.html
3. initialize project cmd line: ```npm init```; follow prompts to create the package.json
4. install express body parser and ejs: ```npm install express body-parser ejs mongoose lodash```
6. run app : ```node server.js```

## Docker 

1. to run : ```docker run -e ME_CONFIG_MONGODB_SERVER=192.168.1.25 -p 8081:8081 mongo-express  ```

## Docker Compose 

run below command to : run node js app, run a mongodb container, mongo express container

1. ```docker-compose up```
2. access node js app on: http://192.168.1.25:3000/
3. access mongodb express  container on: http://192.168.1.25:8081/
