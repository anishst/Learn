# Databases

## MongoDB

- Download - https://www.mongodb.com/download-center/enterprise
- User Manual: https://docs.mongodb.com/manual/

Each database contains collections and then each collection has Documents

|Command | Description |
|--------|--------------------|
| ```mongod``` | start mongodb server|
| ```mongo``` | interact with db|
|```mongo --version```|shows version of mongo shell|
| ```show dbs```| shows databases|
| ```use dbname``` | use a database; this also creates db if it doesn't exists|
|```show collections``` | shows collections|
| ```db.lists.find({}, {name:1})```| get only name columns|
|```db.student.find({}, {roll:1, _id:0})```|get all data from one field without _id|
| ```dbo.students.insert({"name})```| insert data|
|```db.lists.find().count()``` | count of items in database|
|```db.lists.drop()```| clears the lists collection|


- array updates: https://docs.mongodb.com/manual/reference/operator/update/positional/

### MongoDB Atlas

- cloud version of mongodb 
- https://www.mongodb.com/cloud/atlas
- steps to create
    - create a new cluster at : https://cloud.mongodb.com/
    - add a new user to the cluster; admin acct
    - configure ip addresses
    - connect to cluster using connect option and follow prompts
    - to connect from app: ```mongodb+srv://<username>:<password>@cluster0.ykfwk.mongodb.net/<dbname>?retryWrites=true&w=majority```
- MongoDB GUI
    - Robo 3T - https://robomongo.org/

### Docker Usages

- Use MongoExpress to view items:https://hub.docker.com/_/mongo-express
    - run docker container: ```docker run -e ME_CONFIG_MONGODB_SERVER=<mongo_db_ip> -p 8081:8081 mongo-express```
    - view url: ```<docker_machine_ip>:8081/```