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

• image is the application we want to run
•container is an instance of that image running as a process
•possible to have multiple containers running of the same image
•dockers default image "registry" is called Docker Hub

Registries and Repositories

- registry is where we store our images
- you can host your own registry or can use dockers publich registry
called Docker Hub
https://hub.docker.com/



## Steps to Install - Windows

Docker for windows - windows 10 machines; has built-in VM; preferred method
Docker Toolbox - windows version older than win10

1.Download docker https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows
2.Download URL: https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe
3.After install make sure to switch to Windows Containers

## Running a test container (busybox):

docker run busybox:1.24
docker run busybox:1.24  echo "Hello world"
docker run busybox:1.24 ls / - shows directories in the root directory of image
docker run -i  -t busybox:1.24 - run container in interactive mode; similiar to running cmd windows inside container
    in this mode you can type in commands just like cmd window
    to exit type exit
    this will shutdown the container and thus overriding any changes

    
Docker Network defaults
=======================
- each container connected to private virtual network bridge


Docker Commands
===========================

docker stop — Stops one or more containers. docker stop my_container stops one container, while docker stop $(docker ps -a -q) stops all running containers.

## Docker File


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
To run yaml file: docker-compose up -d

to stop all: docker-compose stop