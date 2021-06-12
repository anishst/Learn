# Node JS App with Docker

1. new project: ```npx create-react-app frontend```; more info: https://create-react-app.dev/docs/getting-started
2. some commands:
    - to run dev server: ```npm run start```
    - to run tests: ```npm run test```
    - to build for production: ```npm ```

3. create dev docker file
4. build with tag reactapp and custom dockerfile: ```docker build -t reactapp -f Dockerfile.dev .```
5. start dev server: ```docker run -it -p 3000:3000 reactapp```
6. to run tests: ```docker run -it -p 3000:3000 reactapp npm run test```
7. to run with port mapping in windows 10; this allows live code changes being reflected; good for development: ```docker run -it -p 3000:3000 -v /app/node_modules -v  %cd%:/app reactapp```

## Run app with docker compose for dev

1. create yaml file
    ```yaml
    version: '3'
    services:
    web:
        build:
            context: .
            dockerfile: Dockerfile.dev
        ports: 
            - "3000:3000"
        volumes:
            - /app/node_modules
            - .:/app
    tests:
        build:
            context: .
            dockerfile: Dockerfile.dev
        volumes:
            - /app/node_modules
            - .:/app
        command: ["npm", "run", "test"]

    ```
2. to run do ```docker-compose up```


## For production build - multi-step build

1. create prod docker file

    ```yaml
    FROM node:alpine as builder
    WORKDIR '/app'
    COPY package*.json ./
    RUN npm install
    COPY . .
    RUN npm run build

    FROM nginx
    EXPOSE 8001 # using 8001 to avoid conflict; normally 80
    COPY --from=builder /app/build /usr/share/nginx/html
    ```
2. build prod image by: ```docker build .```
3. run : ```docker run -p 8001:80 <containerid>``` and see the app at: http://192.168.1.50:8001/