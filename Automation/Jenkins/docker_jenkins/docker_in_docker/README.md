# Docker in Docker Scenario

https://itnext.io/docker-in-docker-521958d34efd

1. build custom image:

````dockerfile
# for testing a docker within docker secarios
FROM jenkins/jenkins:lts

# switch to root user
USER root

# show which user is running
RUN uname -a && cat /etc/*release

# Istall docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

RUN apt-get update \
    && apt-get install -y sudo \
    && rm -rf /var/lib/apt/lists/*

# set jenkins and docker users
RUN usermod -a -G root jenkins

RUN usermod -aG docker jenkins

# switch back to jenkins user
USER jenkins
````

2. build image: ```docker build . -t jenkinsdocker```
3. run image with bind mount to use host docker: ```docker run -ti -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 -p 50000:50000 -u root jenkinsdocker:latest```
