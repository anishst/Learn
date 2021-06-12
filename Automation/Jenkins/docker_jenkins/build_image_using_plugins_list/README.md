# Build Custom Jenkins Master Image Using Plugins list

1. get list of plugins from stable jenkins instance using jenkins script console

    ```groovy

    List<String> jenkinsPlugins = new ArrayList<String>(Jenkins.instance.pluginManager.plugins);
    //println(jenkinsPlugins)
    jenkinsPlugins.sort { it.displayName }
        .each {plugin ->
            println("${plugin.shortName}:${plugin.version}")
        }

    ```

2. create docker file

    ```dockerfile

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


    ```

3. build image with tag: ```docker build . -t jenkinsmasterwithplugins```
4. spin up container using new image: ```docker run -p 9000:8080 -p 50001:50000 jenkinsmasterwithplugins```

5. to make it is easy use docker-compose file to; this will 

    ```yaml
    version: "3.7"

        services: 
            jenkins:
                # image: jenkins/jenkins:lts
                image: jenkinsmasterwithplugins:latest # using custom image
                environment: 
                    JAVA_OPTS: -Djenkins.install.runSetupWizard=false
                    JENKINS_OPTS: --argumentsRealm.roles.user=admin --argumentsRealm.passwd.admin=admin, --argumentsRealm.roles.admin=admin
                ports: 
                    - 9000:8080
                volumes: 
                    - /var/run/docker.sock:/var/run/docker.sock
                build: 
                    context: .
    ```