# How to Connect to mysql Docker from Python application


## Step 1. start the docker container by running the following

```docker run --name=user_mysql_1 --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest```


## Step 2. To access mysql inside your docker container, do the following.

```docker exec -it user_mysql_1 mysql -uroot -proot_password```

create db by running following: ```CREATE DATABASE test_db;```
switch to db: ```use test_db;```
create a table: ```CREATE TABLE test_table (userId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(20), lastName VARCHAR(20));```

## Step 3. create a new user

create a user to interact with that database. As best practice, we should never use the root user to do our work. We should only use root user if we really have to, e.g. to create a new database, to create a new user.

```CREATE USER 'newuser'@'%' IDENTIFIED BY 'newpassword';```

grant a sort of admin access to newuser to manage the database test_db.

```GRANT ALL PRIVILEGES ON test_db.* to 'newuser'@'%';```

Instead of specifying an ip address, notice the '%'. This is to allow remote connection from anywhere via user newuser.

[source](https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa?source=email-620923261e30-1595917692897-digest.reader------0-59------------------be714f7e_a8ba_4861_8368_d68b5513e029-16-----)

Database is now ready

## Step 4. Write Python Script to Connect to mysql Docker

pip install sqlalchemy pymysql cryptography

run script
