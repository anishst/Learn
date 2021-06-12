https://qxf2.com/blog/docker-container-for-hosting-flask-app/

1. build using Dockerfile: ```docker build --tag cars-api-docker .``` or directly from github: ```docker build --tag cars-api-docker https://github.com/qxf2/cars-api.git#master```
2. run image: ```docker run -p 5000:5000 cars-api-docker```
3. test app: ```http://localhost:5000``` or use curl: ```curl http://127.0.0.1:5000```
4. see data ```curl -u qxf2:qxf2 http://127.0.0.1:5000/cars```