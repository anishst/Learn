# Docker
Docker is an open platform for developing, shipping, and running applications. 
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

https://hub.docker.com/
https://kitematic.com/

- software container
- NOT a VM; docker engine takes care of OS
- Engine shares kernel with diff containers

## Hypervisor-based Virtualization

providers: VMWare, VirtualBox, Hyper-V

Benefits:
- cost-efficient
- easy to scale
Limitation:
- kernerl resource duplication
- application portability issue

## Container-based Virtualization

Benefits:
-runtime isolation
-cost-efficient
-less memory 
-fast deployment
-guarateed portability


## Docker Architecture

- **image** is the application we want to run
- **container** is an instance of that image running as a process
- possible to have multiple containers running of the same image
- dockers default image "registry" is called Docker Hub
- images are created using a DockerFile

Registries and Repositories

- registry is where we store our images
- you can host your own registry or can use dockers publich registry
called Docker Hub
https://hub.docker.com/



## Steps to Install - Windows

Docker for windows - windows 10 machines; has built-in VM; preferred method
Docker Toolbox - windows version older than win10

1. Download docker https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows
2. Download URL: https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe
3. After install make sure to switch to Windows Containers


 Steps to Install - Ubuntu

https://docs.docker.com/install/linux/docker-ce/ubuntu/
get

Different ways to install; easy one is to Install using the convenience script

Issue: Get error "docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.35/containers/create: dial unix /var/run/docker.sock: connect: permission denied.See 'docker run --help'"

Solution: add user to docker group ```sudo usermod -aG docker $USER```
reboot machine. Test by doing ```docker run hello-world```

## Running a test container (busybox):

- docker run busybox:1.24
- docker run busybox:1.24  echo "Hello world"
- docker run busybox:1.24 ls / - shows directories in the root - directory of image
- docker run -i  -t busybox:1.24 - run container in interactive mode; similiar to running cmd windows inside container
    in this mode you can type in commands just like cmd window
    to exit type exit
    this will shutdown the container and thus overriding any changes

    
## Docker Network defaults

- each container connected to private virtual network bridge


## Docker Commands

https://docs.docker.com/engine/reference/run/

|Command | Description 
|--------|--------------------|
|docker run *image*| runs the images; if not downloaed it will download |
|docker ps | lists all running containers|
|docker ps -a | lists all containers|
|docker ps -aq| list all container ids |do
|docker images| shows images|
|docker stop *containerid/name* | Stops one or more containers|
|docker stop $(docker ps -a -q)  |stops all running containers. |
|docker stop *my_container*|stops one container name *my_container* |
|docker rm $(docker ps -a -q)| remove all stopped containers|
|docker rmi -f *image_id*| force deletion of image|
|docker rmi $(docker images -q) | Remove all images |
| **Publishing Images**||
|docker login| to login to docker account|
|docker push *accountname/imagename*| pushes image to docker hub|
| **Get environment variables**||
|docker inspect *containername*| check under config > env section to get variales|

## Launch Common Apps

- ```docker container run --publish 80:80 nginx``` - run nginx web server in attach mode
- ```docker container run --publish 80:80 nginx``` - un nginx web server in detached mode

## Docker File

```
FROM php:7.0-apache
COPY src/ /var/www/html
EXPOSE port 80
```


Compose is a tool for defining and running multi-container Docker applications

Sample YAML File

docker-compose.yml
```
    seleniumhub:
        image: selenium/hub
        ports: 
            -4444:4444

    firefoxnode:
        image: selenium/node-firefox-debug
        ports:
            -4577
        links:
            - seleniumhub:hub

    chromenode:
        image: selenium/node-chrome-debug
        ports:
            -4578
        links:
            - seleniumhub:hub
```
To run yaml file: ```docker-compose up -d```

to stop all: ```docker-compose stop```
## Common Containers and setup

### Jenkins
 
https://github.com/jenkinsci/docker/blob/master/README.md



## Troubleshooting

- https://success.docker.com/article/docker-for-windows-fails-with-a-daemon-not-running-message