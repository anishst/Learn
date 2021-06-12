# Python FAST API in Docker

- https://fastapi.tiangolo.com/

- https://medium.com/swlh/python-with-docker-fastapi-c4c304c7a93b

- https://medium.com/swlh/python-with-docker-compose-fastapi-part-2-88e164d6ef86

- https://github.com/ahmednafies/fastapi_docker

This uses pipenv


1. run app
2. go to: http://localhost:8000/docs

## with docker

1. build: ```docker build -t fastapi_example .```
2. run: ``` docker run --name app -p 8000:8000 fastapi_example```

## with docker compose
1. add yaml
    ```yaml
    version: "3"
    services:
      postgres:
        image: postgres:11
        ports:
          - "5432:5432"
        environment:
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=postgres
          - POSTGRES_DB=postgres
      web:
        build: ""
        volumes:
          - .:/code
        ports:
          - "8000:8000"
        depends_on:
          - postgres
    ```
 2. build: ```docker-compose up --build```


 ## add pgadmin 
 
 1. add another container for pgadmin4 which is a graphical interface management tool for postgres

    ```yaml
    version: "3"
    services:
    postgres:
        image: postgres:11
        ports:
        - "5432:5432"
        environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
        - POSTGRES_DB=postgres
    app:
        build: .
        volumes:
        - .:/code
        ports:
        - "8000:8000"
        depends_on:
        - postgres
    pgadmin:
        container_name: pgadmin
        image: dpage/pgadmin4
        environment:
        - PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org
        - PGADMIN_DEFAULT_PASSWORD=admin
        ports:
        - "5050:80"
        depends_on:
        - postgres
    ```
2. go to: http://localhost:5050
3. login with ```pgadmin4@pgadmin.org``` and ```admin``` pwd
4. create a new db server 
    - connection
        - host: postgres
        - use values defined under postgress env

## if caching is needed add below to yaml file

```
redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"
```

stop all using: ```docker-compose down```