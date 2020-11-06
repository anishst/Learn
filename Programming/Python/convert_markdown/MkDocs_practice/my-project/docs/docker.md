# Docker
Docker is an open platform for developing, shipping, and running applications. 
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

https://hub.docker.com/
https://kitematic.com/

History: https://www.youtube.com/watch?time_continue=1882&v=Q5POuMHxW-0&feature=emb_logo


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

- **container** 
    - applications run in containers
    - is an instance of that image running as a process
    - multiple containers can be created using same image
- **images** 
    - is the application we want to run
    - how we start containers
- dockers default image "registry" is called Docker Hub
- images are created using a DockerFile
- **Dockerfiles** 
    - series of commands to build an image
- **Docker Engine**
    - manages containers on your machine
    - Docker CLI - command line interface
    - REST API
    - Docker Deamon
    - namespaces are used to isolate containers
 - **Docker Hub**  
    - common registry of docker images
    - you can host your own registry or can use dockers publich registry called Docker Hub https://hub.docker.com/



## Docker Storage

 - /var/lib/docker
 - C:\ProgramData\DockerDesktop
 - C:\ProgramData\Microsoft\Windows\Hyper-V\Virtual Machines
 - C:\Users\Public\Documents\Hyper-V\Virtual hard disks
 - laytered architecture - saves disk space
 - volumes
  - 2 types of mounting
    - volume monting - from volume folder
    - bind mounting - location from host

## Steps to Install - Windows

Docker for windows - windows 10 machines; has built-in VM; preferred method
Docker Toolbox - windows version older than win10

pre-reqs: https://docs.docker.com/docker-for-windows/install/#system-requirements

1. Download docker https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows
2. Download URL: https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe
3. After install make sure to switch to Windows Containers
4. Test using below command ```docker run hello-world```; should ge a "Hello from Docker!" msg


## Steps to Install - Ubuntu

https://docs.docker.com/install/linux/docker-ce/ubuntu/
get

Different ways to install; easy one is to Install using the convenience script

Issue: Get error "docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.35/containers/create: dial unix /var/run/docker.sock: connect: permission denied.See 'docker run --help'"

Solution: add user to docker group ```sudo usermod -aG docker $USER```
reboot machine. Test by doing ```docker run hello-world```

## Steps to install - Debian

### Install Docker
1.Following steps: https://docs.docker.com/engine/install/debian/

Test by running: ```sudo docker run hello-world```

When running docker ps you might get this error: "Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/images/json: dial unix /var/run/docker.sock: connect: permission denied"
Fix by adding user to docker group: ```sudo usermod -aG docker <username>```

### Install Docker compose

Follow steps for Linux: https://docs.docker.com/compose/install/


## Running a test container (busybox):

- docker run busybox:1.24
- docker run busybox:1.24  echo "Hello world"
- docker run busybox:1.24 ls / - shows directories in the root - directory of image
- docker run -i  -t busybox:1.24 - run container in interactive mode; similiar to running cmd windows inside container
    in this mode you can type in commands just like cmd window
    to exit type exit
    this will shutdown the container and thus overriding any changes

    
## Docker Networking

- When you spawn a container via docker run you can define a network by adding --network={your-network-name-here} (or the shortcut -n)
- each container connected to private virtual network bridge
- All containers that spawn without a network definition are connected automatically to the default bridge network.

## Permissions and User/Group Mappings
-  Any file that is created gets associated, by default, with the user and group 0 (the root user/group mapping). This means that you can't edit or delete them on your host computer without using sudo or running a chown command to remap the file's permissions to your own user.
- ```--user {user}:{group}``` to associate the files to our account
- use id -u to get the user and id -g to get the group
    - ```docker run --user $(id -u):$(id -g) {the rest of your command here}```
## Docker Commands

- https://docs.docker.com/engine/reference/run/
- https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421

|Command | Description 
|--------|--------------------|
|docker info| details about docker install|
|docker system prune |Delete all unused containers, unused networks, and dangling images. |
|docker system prune -a --volumes|*-a* is short for --all. <br/>Delete unused images, not just dangling ones. <br/> *--volumes* Remove unused volumes. |
| **Image Related**|
|docker image build -t my_repo/my_image:my_tag . | Build a Docker image named my_image from the Dockerfile located at the specified path or URL|
|docker image push my_repo/my_image:my_tag | Push an image to a registry.|
|docker run *image*| runs the images; if not downloaed it will download |
|docker images| shows images|
|docker image ls | List your images. Shows you the size of each image, too.|
|docker image history my_image | Display an image’s intermediate images with sizes and how they were created.|
|docker image inspect my_image | Show lots of details about your image, including the layers that make up the image.|
|docker stop *my_container*|stops one container name *my_container* |
|docker rm $(docker ps -a -q)| remove all stopped containers|
|docker rmi -f *image_id*| force deletion of image|
|docker rmi $(docker images -q) | Remove all images |
| docker history Imagename| shows how the image was built|
| **Docker Hub Related**|
| docker tag *yourimagename* *yourdockerhubid/yourimagename*| to tag a image to get it ready for push to docker hub|
|docker login| to login to docker account|
| docker commit -m "my custom image" containerid tagname | how create a new image from a running/modfified conainer|
|docker push *accountname/imagename*| pushes image to docker hub|
| **CURL usage**|
|curl -I 0.0.0.0:8080| using curl to get info about container|
|curl -I 127.0.0.1:80||
| **Container Related**|
|docker run -d --name mysql mysql| to launch in detached mode wih custom nmae of 'mysql'|
|docker container run -P -d image|The -P command opens every port the container exposes.|
|docker ps | lists all running containers|
|docker ps -a | lists all containers|
|docker container port *insert container_uuid*|get container port mapping; you can also use ```netstat -ntlp```|
|docker ps -aq| list all container ids |do
|docker stop *containerid/name* | Stops one or more containers|
|docker stop $(docker ps -a -q)  |stops all running containers. |
|docker rm $(docker stop $(docker ps -a -q --filter ancestor=nginx --format="{{.ID}}"))| kills all containser with specifc image; ex. nginx|
|docker container kill $(docker ps -q) | Kill all running containers|
|docker container rm $(docker ps -a -q)| deletes all container not running|
|docker inspect *containername*| get info about containers; mappings, env var etc.|
| **Monitoring related**||
| docker stats | shows performance stats
|  docker logs -f *containerid or customname* | shows live logs |
|docker exec *containername* ps -eaf| shows all processes running|
|docker exec -it jenkins bash | log into bash of jenkins container|
| ps -eaf | show processes ids on the host|
| ctl+p then ctrl+q  or ctrl + d| to get out of interactive mode|
| **Monitoring related - Linux**||
| docker info pipe grep -i root |find were docker is installed|
|sudo du -sh /var/lib/docker |find out space used by docker|
| docker diff name| shows changed files|
|docker inspect| low level info about images|
|docker system df|This command shows Docker’s disk usage|
|docker image ls -f dangling=true|list the existing dangling image on the system|
|docker image prune| remove dangling images|
| **VLOUMES**||
| docker volume create *data_volume_name* | creates a new volume under /var/lob/docker/volumes/*data_volume_name*|
| docker run -v *data_volume_name*:/var/lib/mysql mysql
|docker volume rm $(docker volume ls -q)|remove the volumes not used any longer|
|docker volume prune| prune unused vols|
| **Docker Compose**||
|docker-compose down -v | bring down docker containers and prune volumes|
|docker-compose up | build images/setup vol/networks and start all containers|
|docker-compose down | stop all containers and remove cont/vol/net|
|docker-compose logs | show logs|
|docker-compose build| rebuild images|
|docker-compose build -f *customyamlfile* | rebuild images|
|docker-compose ps | shows details when run in same folder|
|docker-compose down --rmi  | bring down docker containers and prune volumes and delete images|

## Launch Common Apps

- ```docker container run --publish 80:80 nginx``` - run nginx web server in attach mode
- ```docker container run --publish 80:80 nginx``` - un nginx web server in detached mode

## Docker for Development

- https://medium.com/better-programming/why-and-how-to-use-docker-for-development-a156c1de3b24
- https://runnable.com/docker/java/dockerize-your-java-application
### Node

Test a simple hello world NodeJS program
1. install dependency: ```docker run --rm -it -v $PWD:/app -w /app node npm install hello-world-npm```
2. creat a test file: hello.js
    ```javascript
    const helloWorld = require('hello-world-npm');
    console.log(helloWorld());
    console.log("Hello Node!");
    ```
3. run app: ```docker run --rm -it -v $PWD:/app -w /app node hello.js```

### Java

1. https://github.com/smartsheet-samples/docker-java-hello-world


## Docker File Use Example - Apache web server

1. create a docker file for apache: https://hub.docker.com/_/httpd
```
FROM httpd:2.4
COPY ./public-html/ /usr/local/apache2/htdocs/
```
2. bring up command window in location of docker file
3. build image with a tag ```docker build -t my-apache2 .```
4. run container: ```docker run -dit --name my-running-app -p 8080:80 my-apache2```
5. go to: ```http://<docker ip address>:8080/``` to see page

## Docker File Use Example - Python Selenium

1. docker file

```buildoutcfg
# create image
FROM debian:latest

# configure with python3 and pip
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install python3 -y \
    python3-pip

# install needed plugins
```
Python Image Guides:
   - https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3

## Docker Compose

- Compose is a tool for defining and running multi-container Docker applications
- way to configure relationships between containers
- versions: 1, 2, 2.1, 3, 3.1; info on version: https://docs.docker.com/compose/compose-file/compose-versioning/
- yaml used with docker-compose command
- command ref: https://docs.docker.com/compose/reference/up/
- enviornment var formats
    - envvarName=value - get during run time from custom file
    - envarname - use directly from computer at run time

Yaml template:
```yaml
version: '3.1' # if no version then v1 is assumed

services: # containers. same as docker run
    servicename: # a friendly name ; dns name in network
      image: # optional if u use build
      command: # optional replace the default CMD specified by image
      enviornment: # optional, same as -e in docker run
      volumes: # optional, same as -v in docker run
    servicename2:

volumes: # optional, same as docker volume create

networks: # optional, same as docker network create
```

- to make it easy to build from github
    - make sure ur repo has Dockerfile and docker-compose.yml
    - then git clone github.com/somerepo
    - docker-compose up
    
### docker-compose CLI

- separate from docker tool
- comes with docker for windows/mac, download sep for linux
- 2 most common commands
    - ```docker-compose up``` # setup vol/networks and start all containers
    - ```docker-compose down``` # stop all containers and remove cont/vol/net
    - ```docker-compose logs``` # show logs


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

### Using Compose to build



### Videos/Git repos
- https://bah.udemy.com/course/docker-mastery/learn/lecture/6775794#overview
- https://github.com/BretFisher/udemy-docker-mastery
## Selenium Grid with Docker

```dockerfile
docker pull selnium/hub:3.14
docker pull selenium/node-firefox:3.14
docker pull selenium/node-chrome:3.14
```
## Container Lifetime & Persistent Data

### Volumes

- a way to save data created in containers even after container is stopped or removed
- share files between host and container; 
- ```docker run -v <hostpath>:<containerpath>```
- volumes needs manual deletion; stopping container won't remove it
- you can see mapping by using  ```docker inspect <name of image>```
- to see list of volumes: use ```docker volume ls```
- to remove all volumes use: ```docker system prune -a --volumes```
#### Named volumes

- friendly way to assign vols to containers
 
example; in this **mysql-db** is the custom name of the volumen: 
 
 ```docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql```
 - see details by: ```docker  volume inspect mysql```
 
 output ```
 [
    {
        "CreatedAt": "2020-05-06T18:31:34Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/mnt/sda1/var/lib/docker/volumes/mysql-db/_data",
        "Name": "mysql-db",
        "Options": null,
        "Scope": "local"
    }
]
      ```
      
### Shell Differences

With Docker CLI, you can always use a full file path on any OS, but often you'll see me and others use a "parameter expansion" like $(pwd) which means "print working directory".

For PowerShell use: ${pwd} 

For cmd.exe "Command Prompt use: %cd%

Linux/macOS bash, sh, zsh, and Windows Docker Toolbox Quickstart Terminal use: $(pwd) 

Note, if you have spaces in your path, you'll usually need to quote the whole path in the docker command.

### Bind Mounting

- maps a host file or directory to a container file or directory
- 2 locations pointing to the same file(s)
- host file overwrite any in container
- can't use in Dockerfile, must be at container run
Example:
    - ```...run -v //c/Users/anish/stuff:/path/container (windows)```
     - ```...run -v /Users/anish/stuff:/path/container (max/linux)```
     
#### nginx bind mount practice - with docker toolbox
1. ownload folder has the index.html that nginx will use
2. run container: ```docker container run -d --name nginx -p 80:80 -v //c/Users/anish/Downloads:/usr/share/nginx/html nginx```
3. verify by going to: ```http://<dockerip>```
4. to make sure it is using your html: ```docker container exec -it nginx bash```
use below commands to view html
```
cd /usr/share/nginx/html
cat index.html
```

### ENTRYPOINT vs CMD

#### ENTRYPOINT
- universal way to do things on container startup 
- use custom entrypoint script
- runs everytime container runs

https://docs.docker.com/engine/reference/builder/#entrypoint

#### CMD

### Docker in Docker

https://itnext.io/docker-in-docker-521958d34efd

### WSL Docker

https://docs.docker.com/docker-for-windows/wsl/

https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/


## AWS and Docker

https://aws.amazon.com/docker/

Elastic Beanstalk is a good option
 
### Troubleshooting
- http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows
- https://rominirani.com/docker-on-windows-mounting-host-directories-d96f3f056a2c
- Windows mapping issue: https://medium.com/@Charles_Stover/fixing-volumes-in-docker-toolbox-4ad5ace0e572
## Networking

- Create network ```docker network create my-network```
- assign network to image: ```docker run -d --name=nginx --network=my-network nginx```

## Common Containers and setup

### Jenkins
 
https://github.com/jenkinsci/docker/blobmaster/README.md

## Training Vidoes
- https://bah.udemy.com/course/selenium-webdriver-with-docker/learn/lecture/13299724?start=285#overview 

## Troubleshooting

- https://success.docker.com/article/docker-for-windows-fails-with-a-daemon-not-running-message
