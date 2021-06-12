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