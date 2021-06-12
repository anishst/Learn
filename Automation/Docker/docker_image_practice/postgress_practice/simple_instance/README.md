# Postgres with Docker

https://hub.docker.com/_/postgres

1. launch an instance using: ```docker run -d -p 5432:5432 -v postgres-data:/var/lib/postgresql/data --name postgres1 postgres```
2. view logs: ```docker logs postgres1```
    - you should see '2020-07-15 01:14:29.426 UTC [1] LOG:  database system is ready to accept connections'
3. launch interactive mode: ```docker exec -it some-postgres sh```
4. to list dbs: ````\l````
