FROM jenkins/jenkins:lts

# copy plugins file to image jenkins plugin location
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

# install plugins
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# run as root user
USER root

# install docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

# show which user is running
RUN uname -a && cat /etc/*release


RUN apt-get update \
    && apt-get install -y sudo \
    && rm -rf /var/lib/apt/lists/*

# set jenkins and docker users
RUN usermod -a -G root jenkins
RUN usermod -aG docker jenkins

# switch back to jenkins user
USER jenkins
