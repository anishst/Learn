# MongoDB

https://hub.docker.com/_/mongo

## Running simple container
docker run -d -p 27017:27017 --name customName mongo

## Running simple container with volume map
on linux: docker run --name some-mongo -v /my/own/datadir:/data/db -d mongo
NOT WORKING on windows: ```docker run --name some-mongo -v //C/Users/ats/docker/mongodb:/data/db -d mongo```



## using docker volume - This works
1. create volume: docker volume create --name=mongodata
2. docker run --name mongodb -v mongodata:/data/db -d -p 27017:27017 mongo

## Running and view database using mongo express
1. run container:  ```docker run --name mongodb -v mongodata:/data/db -d -p 27017:27017 mongo```
2. link mongoexpress: ```docker run --link mongodb:mongo -p 8081:8081 mongo-express```
3. go to : http://192.168.1.50:8081/

## Issues
when using authenication u need to login to create a user first; see this guide: https://medium.com/@anuradhs/how-to-start-a-mongo-database-with-authentication-using-docker-container-8ce63da47a71

https://stackoverflow.com/questions/23943651/mongodb-admin-user-not-authorized

```mongodb


use admin
db.createUser(
  {
    user: 'admin',
    pwd: 'password',
    roles: [ { role: 'root', db: 'admin' } ]
  }
);
exit;
```


## Guides:
- https://blog.jeremylikness.com/blog/2018-12-27_mongodb-on-windows-in-minutes-with-docker/
- compose: https://medium.com/faun/managing-mongodb-on-docker-with-docker-compose-26bf8a0bbae3
- https://dev.to/sonyarianto/how-to-spin-mongodb-server-with-docker-and-docker-compose-2lef