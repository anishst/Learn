# Databases

## MongoDB

- Download - https://www.mongodb.com/download-center/enterprise
- User Manual: https://docs.mongodb.com/manual/

Each database contains collections and then each collection has Documents

|Command | Description |
|--------|--------------------|
| ```mongod``` | start mongodb server|
| ```mongo``` | interact with db|
| ```show dbs```| shows databases|
| ```use dbname``` | use a database; this also creates db if it doesn't exists|
|```show collections``` | shows collections|
| ```dbo.students.insert({"name})```| insert data|
|```db.lists.find().count()``` | count of items in database|
|```db.lists.drop()```| clears the lists collection|


- array updates: https://docs.mongodb.com/manual/reference/operator/update/positional/

### Docker Usages

- Use MongoExpress to view items:https://hub.docker.com/_/mongo-express
    - run docker container: ```docker run -e ME_CONFIG_MONGODB_SERVER=<mongo_db_ip> -p 8081:8081 mongo-express```
    - view url: ```<docker_machine_ip>:8081/```