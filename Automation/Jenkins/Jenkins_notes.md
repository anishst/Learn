# Jenkins

- [Jenkins and Docker](#jenkinsdocker)
- [Docker Agents](#dockeragents)

Jenkins is a self-contained, open source automation server  to automate tasks such as building, testing, and deploying software
- java application
- used for continuous integraton and delivery ( Automated Deployment: Build > Deploy > Test > Release)
- **workspace** - whenever you run job jenkins copies by default copies your code to the workspace folder
    - default workspace location
    - when running using war file: C:\Users\<userid>\.jenkins\workspace\<jobname
    - when isntalled as program: C:\Program Files\Jenkins\workspace
## Basic flow
1. developer checks in code to source control (Git/TFS)
2. Jenkins grabs latest code
3. build artifacts
4. Run tests (Nunit, MSTest, Gradle etc.)
5. Publish output to live server
6. report results

## Pre-requisite
- Java (latest)
- Jenkins war file; Download: https://jenkins.io/download/

## Initial Setup
1. Go to command prompt and in war file folder run this command: ```java -jar jenkins.war```
Note: by default Jenkins will run on port 8080; if you need to use a different port use:  ```java -jar jenkins.war --httpPort=9090```
2. Make a note of the password for setup; towards of the bottom of command window
3. Navigate to: http://localhost:8080 or http://localhost:8080/index
4. Use password to unlock
5. automated plugin install process occurs (Jenkins related file location, like plugins: ```c:\user\.jenkins```)
6. create first admin user


## Ruuning as Windows Service

https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+as+a+Windows+service


## Commands
http://localhost:8080/systeminfo - shows system variabled and values

## Using CLI - Command Line Interface

1. start Jenkins: ```java -jar jenkins.war```
2. In GUI, Go to manage Jenkins > Configure Global Secuirty > check "Enable Security"
3. http://localhost:8080/cli/ - will show the available commands
4. Download the cli jar using step 3 url; you save to any location of your choice
5. 

| Command| Desc   |
|--------|--------|
```java -jar jenkins-cli.jar -s http://localhost:8080/ help``` | shows available commands

## Configuring Jenkins

### Moving Jenkins Home Directory (Optional)

Default Location - windows: ```C:\Users\<username>\.jenkins```
1. check current home directory by starting jenkins and login go to: manage jenkins > configure system > home directory
2.  make a new directory for moving jenkins
3. copy all files from old directory to new directory
4. WINDOWS: change env variable JENKINS_HOME and set to new dir; if none exists create it
5. restart jenkins using command line or by using: http://localhost:8080/restart

## Jenkins Slaves

- in prod, good to have small master node and one or more worker nodes (Jenkins slaves)
-  static or manual scaling based on needs
- dynamic scaling
    - Amazon EC2 plugin
    - Docker plugin - uses docker host to spin up a slave container run a jenkins build in it and tear it down
    - Amazon ECS plugin
    - Digitalocent plugin
- builds can be executed on specific nodes using specific label
- configured via UI or Jenkinsfile
```
node(label: 'windows64-node') {
    {
        stage('build'){
    }
}
}
```
- reduced costs
- master node connects to slave over SSH
- slave node connects to master over JNLP
https://bah.udemy.com/course/learn-devops-ci-cd-with-jenkins-using-pipelines-and-docker/learn/lecture/7249746#overview

### Slave setup

1. On Jenkins master make sure Jenkins > Configure Global Security > Agents > random is selected
2. make sure 'Inbound TCP Agent Protocol/4 (TLS encryption)' is checked
3. On your master machine go to Manage Jenkins > Manage Nodes and Clouds
4. Enter other details
5. go to slave machine and access: ```http://<jenkins server ip>/computer/<name of node>/```
6. download and save agent.jar to jenkins folder
7. to launch enter this command: ```java -jar agent.jar -jnlpUrl http://<jenkins server ip>:8080/computer/win10home_alienware/slave-agent.jnlp -secret 05a0cd9cd337cc20c04b8cfd360d95cfae48da0a045e203b15e2ffca6c8ab17b -workDir "D:\jenkins_slave_data"```

## ssh-agent
- runs on master and contain private keys needed to authenticate to external systems 
- ssh-agent plugin

## Jenkins Security

- basic security enabled
- secure by default
- do security changes to using Global security: http://localhost:9000/configureSecurity/
- check 'Allow users to sign up' if you don't want to manage new user accounts; users can sign up 
- under Authorization, enable 'Allow anonymous read access' if you want readyonly access to users not logged in
- default Authorization is "Logged-in users can do anything"

### Credentials

### scopes

- System - only available on Jenkins server; NOT for jenkins job
- Global - available everywhere ; jobs as well

### types

- username & password
- secret file
- more...

### Matrix Authorization

- under Configure Global Security > Authorization> Matrix-based security
- allows giving specific permission using user/group

### Steps to Disable security If completely locked out of Jenkins
- manually disable security
    - edit config.xml (C:\Users\<userid>\.jenkins\config.xml)
    - this is the primary config file
- comment out below areas 
 
```
<!--
 <authorizationStrategy class="hudson.security.FullControlOnceLoggedInAuthorizationStrategy">
    <denyAnonymousReadAccess>true</denyAnonymousReadAccess>
  </authorizationStrategy>
  <securityRealm class="hudson.security.HudsonPrivateSecurityRealm">
    <disableSignup>true</disableSignup>
    <enableCaptcha>false</enableCaptcha>
  </securityRealm>
-->
```
- set  ```<useSecurity>false</useSecurity>```
- restart Jenkins    
    
### Setting up Role Based Strategy

1. Download Role Strategy Plugin: https://wiki.jenkins.io/display/JENKINS/Role+Strategy+Plugin
Option 1: download .hpi file and put it plugins folder
Option 2: install using plugins from GUI
2. Go to Jenkins > Configure Gloabl Security > check enable security > select "Role-Based Strategy" under Authorization section
3. Manage Roles: Jenkins > manage and assign roles
- create gloal roles
- create project roles
- apply/save
4. Assign Roles: Jenkins > manage and assign roles
- create gloal roles
- create project roles
- apply/save

## Environment Variables

- Usage info: https://jenkins.io/doc/pipeline/tour/environment/
- Get list of vars: http://localhost:9000/env-vars.html/
- usage examples:```pytest test_stability_administration_audit.py --html=${BUILD_NUMBER}_report.html --junitxml="result.xml"```
- ex2: ```pytest test_stability_administration_audit.py --html=reports/build_${BUILD_NUMBER}_report.html --junitxml="reports/build_${BUILD_NUMBER}result.xml"```
- more info: https://wiki.jenkins.io/display/JENKINS/Building+a+software+project
- you can also create Global enviornment variables; set a global environment variable in Manage Jenkins --> Configure System --> Global properties.
# Jobs

## Trigger Jobs remotely
1. In the Job configuration,enable "Trigger builds remotely
2. set Authentication Token	and apply changes
3. use the url with token to run job remotely:  JENKINS_URL/job/Test/build?token=TOKEN_NAME; Example: http://localhost:8080/job/Test/build?token=1234

Linux example: https://bah.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/13085766#overview
```shell script
SERVER=http://localhost:8080
CRUMB=$(curl --user $USER:$APITOKEN \
    $SERVER/crumbIssuer/api/xml?xpath=concat\(//crumbRequestField,%22:%22,//crumb\))
curl --user $USER:$APITOKEN -H "$CRUMB" -d "script=$GROOVYSCRIPT" $SERVER/script
```

## Chaining jobs
1. in build triggers section select "Build after other projects are built" and select the projects to watch
2. Use Add post-build action to to kick off another 

## Parameterize

1. choose This project is parameterized option
2. add values
3. windows batch command syntax: ```pytest --browser %browserName%  test_stability_administration_audit.py```
4. shell command syntax ```pytest --browser $"browserName"  test_stability_administration_audit.py```

## Views (Tabs)

- helps to group jobs


## Pipelines

- collection of jobs
- workflow to acheive CI/CD
- **Build Pipeline plugin** - good for small projects
    - create a new Build Pipeline View in Jenkins (use + iconb)
    - select the initial job to run under 'Pipeline Flow'
    - select number of builds to display under Display Options
- **Jenkins pipeline project** - good for large project
    - uses groovy scripts
    - Groovy DSL (Domain Sepcific Language)
        - declarative pipeline syntax
            - preferred method
            - Allows restart from stage
        - scripted pipline syntax
- **Jenkinsfile**
    - Jenkinsfile is just a text file where we write pipeline code to define the Jenkins pipeline. It can be checked into source control like Git along with our project source code
    
- **Jenkins Shared Library**
    -  shared library, which can be used across applications.
    - [Configure Shared Library in Jenkins](https://www.lambdatest.com/blog/use-jenkins-shared-libraries-in-a-jenkins-pipeline/)
### Scripted pipeline examples

```groovy
node {
    stage("Build"){
        echo "Building"
    }

    stage("Test"){
        echo "Testing"
    }
}

```
### Declarative pipeline examples

#### Pipeline script (Jenkinsfile) simple example 1:
```groovy
pipeline {
   agent any            # where to execute; nodes

   stages {              # where work happens
      stage('Build') {
         steps {
            echo 'Hello World build steps'
         }
      }
   }

   stage('Deploy') {
         steps {
            echo 'Hello World deploy steps'
         }
      }
    
    stage('Test') {
         steps {
            echo 'Hello World Test steps'
         }
      }
    
    stage('Release') {
         steps {
            echo 'Hello World Release steps'
         }
      }
    post {
        always {
            echo "always get executed no matter build status"
        }
        sucesss{
            echo "on sucess only"
        }
        failure{
            echo "on fail only"
        }
    }

}
```

### custom function

```groovy

pipeline {
   agent any

   stages {
      stage('Custom Fun step') {
         steps {
            // use my func
            script {
                val = my_func()
                println(val)
            }
         }
      }
   }
}

def my_func(){
    return "hello world"
}

```
### Capture output from other steps

```groovy

pipeline {
   agent any

   stages {
      stage('Hello') {
          environment {
            //   count how many files in tmp folder; by default sh doens't return so need to use script
              COUNT_FILES = sh(script: "ls -la /tmp | tail -n +4 | wc -l", returnStdout:true).trim()
          }
          
         steps {
            echo "There are ${env.COUNT_FILES} files in /tmp folder"
         }
      }
   }
}

```
### Using Timeout and timestamps

```groovy
pipeline {
    agent any
    options {
        timestamps()
        ansiColor("xterm")
    }

    stages {
        stage("Build") {
            options {
                timeout(time: 1, unit: "SECONDS")
            }
            steps {
                sh 'printf "Hellow world"'
                sh "sleep 5s"
            }
        }
    }
}
```

### Using conditional statements


```groovy
stage('Test') {
    when {
        expression {
            // check git branch and do this stage only when dev or master
            BRANCH_NAME == 'dev' || BRANCH_NAME == 'master'
        }
    }
         steps {
            echo 'Hello World Release steps'
         }
}
```

```groovy

CODE_CHANGES = getGitChanges() // groovy script to check if changes 

stage('Build') {
    when {
        expression {
            // build only if changes
            BRANCH_NAME == 'dev' &&  CODE_CHANGES == true
        }
    }
         steps {
            echo 'Hello World Release steps'
         }
}
```
### parallel stages

```groovy
stage("Parallel") {
  steps {
    parallel (
      "Taskone" : {
        //do some stuff
      },
      "Tasktwo" : {
        // Do some other stuff in parallel
      }
    )
  }
}
```

### send and email and push to MS teams channel

```groovy

  post {
        always {
            echo 'I will always say Hello again!'
        }
        success {
                mail to: 'some@domain.com',
             subject: "Passed Pipeline: ${currentBuild.fullDisplayName}",
             body: "All good with ${env.BUILD_URL}"

            office365ConnectorSend (
            status: "SUCESS",
            //webhookUrl: "<url>",
            webhookUrl: "${MSTEAMS_HOOK}",
            color: '00ff00',
            message: "Test Successful: ${JOB_NAME} - ${BUILD_DISPLAY_NAME}<br>Pipeline duration: ${currentBuild.durationString}"
          )
        }
        failure {
          mail to: 'some@domain.com',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong with ${env.BUILD_URL}"

            office365ConnectorSend (
            status: "FAILED",
            //webhookUrl: "<url>",
            webhookUrl: "${MSTEAMS_HOOK}",
            color: 'd00000',
            message: "Test Failed: ${JOB_NAME} - ${BUILD_DISPLAY_NAME}<br>Pipeline duration: ${currentBuild.durationString}"
          )
        }
    }
```
### Environment variable usage

- jenkins default: vars: http://localhost:9000/env-vars.html/


```
pipeline {
   agent any

   // env defined here will be available to all stages
    
   environment {
        NEW_VERSION = '3.3.1.0'
        SERVER_CREDENTIALS = credentials('server-credentials')
    }

   stages {
      stage('Building Hello World') {
         steps {
            echo 'building app'
            // Use env var; use double quotes to interpret var
            echo "Build version ${NEW_VERSION}"
            
         }
      }

   stage('Deploy') {
         steps {
            echo 'Hello World deploy steps'
         }
      }
         stage('Test') {
         steps {
            echo 'Hello World Test steps'
         }
      }
        stage('Deploy') {
         steps {
            echo "Deploying with ${SERVER_CREDENTIALS}"
      
         }
      }

}
}
```
### copy files into workspace

this example copies csv files from source files dir
```groovy
dir("c:/sourcefiles") {
    fileOperations([fileCopyOperation(excludes: '', flattenFiles: true, includes: '*.csv', targetLocation: "${WORKSPACE}")])
}
```

### Pipeline script (.jenkinsfile) java program example 1:

```groovy
pipeline {
   agent any

   stages {
      stage('Building Hello World') {
         steps {

            bat 'javac Hello.java' // not working
            bat 'java Hello'   // not working

         }
      }

   stage('Deploy') {
         steps {
            echo 'Hello World deploy steps'
         }
      }
         stage('Test') {
         steps {
            echo 'Hello World Test steps'
         }
      }
       stage('Release') {
         steps {
            echo 'Hello World Release steps'
         }
      }
}
}

```

### Spring Boot Pipeline

```groovy
pipeline {
       agent any
       tools {
           maven 'Maven 3.5.0'
           jdk 'jdk8'
       }
       stages {
           stage("Tools initialization") {
               steps {
                   sh "mvn --version"
                   sh "java -version"
               }
           }
           stage("Checkout Code") {
               steps {
                   git branch: 'master',
                       url: "https://github.com/iamvickyav/spring-boot-data-H2-embedded.git"
               }
           }
           stage("Cleaning workspace") {
               steps {
                   sh "mvn clean"
               }
           }
           stage("Running Testcase") {
              steps {
                   sh "mvn test"
               }
           }
           stage("Packing Application") {
               steps {
                   sh "mvn package -DskipTests"
               }
           }
       }
 }
```

### Using differnet docker images in a stage

```groovy
pipeline {
    agent {
        dockerfile {
            label 'Docker'
        }
    }
    environment {
        CSN_RUN_FLAG = "YES"
    }
    stages {


         stage('Unit Tests'){
            steps {
                dir("${env.WORKSPACE}") {
                    echo "Running Unit Tests...."
                    sh "mvn test -Dtest=UserTest"

                 }
            }
        }
        stage('Integration Tests'){
            steps {
                dir("${env.WORKSPACE}") {
                    echo "Running Integration Tests...."
                    sh "mvn clean verify"

                 }
            }
        }
        stage('Performance Tests'){
            agent {
                // https://hub.docker.com/r/justb4/jmeter/
                docker { image 'justb4/jmeter'}
            }
            steps {
                dir("${env.WORKSPACE}") {
                    echo "Running Jmeter Tests...."
                    sh "jmeter -v"
    
                 }
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying Code..."
                echo "Deployment Completed!"
            }
        }
    }

        post {
            always {
                // record test results
                // junit '**/XMLReports/*.xml'
                junit '**/surefire-reports/*.xml'
                // archive artifacts
                archiveArtifacts 'target/*.jar'
            }
        }
}

```
### Pipeline vidoes

- https://www.youtube.com/watch?v=7KCS70sCoK0&t=1106s


## Integration with Git

https://www.youtube.com/watch?v=bGqS0f4Utn4&list=PLhW3qG5bs-L_ZCOA4zNPSoGbnVQ-rp_dG&index=8
1. Create a sample java program
2. start Jenkins
3. Create a job in jenkins to execute the program
4. In the build section, add commands required to run the program.
5. Add project to Git and GitHub by doing following commands from project dir:
```'
git status
git add .
git commit -m "added code"
git remote add origin https://github.com/anishst/HelloWorld.git
git push -u origin master
```
6. In Jenkins, for the job, under Source Code Management section, select "Git" 
7. Under Build Triggers, select "Poll SCM" and a schedule (ex. * * * * *)
    - provide repo urlst
8. apply changes
9. From now on when changes are made Jenkins will automtically kick of a run

## Doing a Maven build - Freestyle project

1. Download practice repo: https://github.com/anishst/time-tracker
2. Test project in command line before test in Jenkins:
    - In project directory run cmd: ```mvn clean package```; compile your code and also package it. For example, if your pom says the project is a jar, it will create a jar for you when you package it and put it somewhere in the target directory (by default).
    - make sure BUILD SUCCESS is shown
3. launch Jenkins
4. create a new project
    - free style
    - point to maven github
    - build batch command: ```mvn clean package``` OR use *Invoke top-level Maven targets* option and select maven instance and command ```clean pakcage```

## Doing a Maven build - Maven plugin project    
 
 https://plugins.jenkins.io/maven-plugin/
 
 1. Download practice repo: https://github.com/anishst/time-tracker
2. launch Jenkins
3. create a new Maven project
4. point to github repo
5. under build, pom.xml should be there; populate clean package for goals and options

## Doing Automated Deployment to Tomcat

### Setup Tomcat
1. Download Tomcat: https://tomcat.apache.org/
    - Use version 9 32-bit/64-bit Windows Service Installer: https://tomcat.apache.org/download-90.cgi
    - during install port change default of 8080 to 9080 to avoid clash with Jenkins/or other ports being used
    - use tomcat as username and pssword
    - for JVM, point to JDF folder
    - finish setup process with defaults
2. check if it is up and running: http://localhost:9080/
3. stop Tomcat by going to Services: Apache Tomcat 9.0 Tomcat9
4. add jenkins as user by editing: 
    - ```C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf\tomcat-users.xml```
    -  add this below to existing username section: ```<user username="jenkins" password="jenkins" roles="manager-script" />```
5. make sure you can access this with jenkins script role account: http://localhost:9080/manager/text/list

Expected output:
```
OK - Listed applications for virtual host [localhost]
/:running:0:ROOT
/host-manager:running:0:host-manager
/manager:running:1:manager
/docs:running:0:docs
```

### Setup Jenkins

- install Deploy to container plugin: https://wiki.jenkins.io/display/JENKINS/Deploy+Plugin or install using Jenkins GUI (Deploy to container)
- in tthe project you want to deploy, under Post-build actions > Deploy war/ear to a container :
    - for WAR/EAR files enter: **/*.war  
    - for Context path: /demo
    - cotainers dropdown: select Tomcat 8.x
    - tomacat Url: http://localhost:9080/
    - select credentials > add > Jenkins
    - Jenkins Credentials Provider: Jenkins comes up
        - enter username: jenkins
        - password: jenkins
        - ID: tomcat-manager-scripts
        - description: Login username and password for local Tomcat server script manager
        - click Add
    - Select credentials item and make sure tomcat url is populated: http://localhost:9080/
 - click Save button
 - Run the build
 - go to: http://localhost:9080/manager/text/list
 if buidl was success you should see:
 ```shell script
OK - Listed applications for virtual host [localhost]
/:running:0:ROOT
/host-manager:running:0:host-manager
/demo:running:0:demo
/manager:running:0:manager
/docs:running:0:docs
```
- You can test app by going to : http://localhost:9080/demo/
### Resources:
-  Dowload sample war file to use with Tomcat: https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/

## Triggering builds

- push notification: version control notifies Jenkins on new commit
- polling: Jenkins polls at regular intervals

## Jenkins Selenium Job

1. Create a freestyle project: Testing Selenium Run
2. choose Use custom workspace and set to project root
3. under build, choose "Execute windows batch command" and enter as shown below:
```shell script
cd tests\Stability
pytest test_stability_administration_audit.py --browser ie --html=reports/build_${BUILD_NUMBER}_report.html --junitxml="reports/build_${BUILD_NUMBER}result.xml"
```
4. for reports, under post-build actions, choose Publish junit test result report and enter "Test Report XML" value as: ```tests/Stability/reports/*.xml``` 

## AWS Lightsail for Jenkins (Cloud-based Jenkins)

- https://aws.amazon.com/lightsail/
- based on AWS resources; less complex
- Like a VPS (Virtual Private Server) on Amazon

## Install Jenkins on AWS EC2

### Overall steps:

AWS
1. create aws account
2. create default vpc and subnets
3. create AMI with Java and docker
4. create new key pair for SSH Access
5. Jenkins - install EC2 instance
6. create Jenkins IAM user
    - IAM > Add user 
        - programmatic access
        - permissions - give needed permissions
        - download CSV file with access key
7. request spot fleet

Jenkins

1. Install EC2 Fleet plugin for Jenkins on Jenkins server
2. add amazon jenkins user using jenkins credentials > AWS Credentials
2. add EC2 user using jenkins credentials > SSH Usrname with private key
    - https://bah.udemy.com/course/selenium-webdriver-with-docker/learn/lecture/14317278#overview
3. go to Jenkins > config >  cloud > amazon spot fleet > select aws creds and fill in reqired fields
    - https://bah.udemy.com/course/selenium-webdriver-with-docker/learn/lecture/14317720#overview

- https://github.com/yankils/Simple-DevOps-Project/blob/master/Jenkins/Jenkins_Installation.MD
- https://bah.udemy.com/course/valaxy-devops/learn/lecture/15772976#overview


## <a name="jenkinsdocker"></a>Jenkins and Docker

```docker run -p 8080:8080 -p 50000 50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts```
-- ```docker logs``` will give initial password
- Guide: https://jenkins.io/doc/book/installing/#docker


docker run -p 8080:8080 -p 50000:50000 -v ~/jenkins_home:/var/jenkins_home jenkins/jenkins:lts


## Jenkins Docker - Debian basic Jenkins container setup

1. Install Debian VM in Virtualbox
2. create a folder jenkins_data
3. Create subfolder for saving jenkins data: jenkins_home
4. in the jenkins_data folder create below yaml file
docker-compose.yml
```yaml
version: '3'

services:
  jenkins:
    container_name: jenkins
    image: jenkins/jenkins
    ports:
     - "8080:8080"
    volumes:
     - "$PWD/jenkins-home:/var/jenkins_home"
    networks:
    - net
networks:
  net:
```
5. run by doing docker-compose up
6. you should be able to access Jenkins on host machine: <vm ip>:8080; you can find vm ip by doing command ```ip a``` inside virtual machine

### Create bash script to use in Jenkins

1. create a script; this print name provided
```vi script.sh
#!/bin/bash
NAME=$1
LASTNAME=$2
echo "hello $NAME $LASTNAME"
```

2. give exe permission: ```chmod +x ./script.sh```
3. test ./script.sh Anish Sebastian
4. copy to docker jenkins image: ```docker cp script.sh jenkins:/tmp/script.sh```
5. go into container: ```docker exec -it jenkins bash ```
5. see file by: ```cat /tmp/script.sh```
6. execute: ``` /tmp/script.sh Anish Sebastian```

### Docker SSH Server for executing Jenkins docker on another container

https://wiki.debian.org/SSH#Installation_of_the_server
https://hub.docker.com/_/debian

Step 1: 
create dir for ssh server container: mkdir debianos
jenkins-data/debianos

create ssh key under new folder
ssh-keygen -f remote-key
enter
enter

creates 2 files: remote-key remote-key.pub
cat remote-key to get the public key

Step 2: create docker file to create SSH server container 
```dockerfile
FROM debian
# install open ssh server
RUN apt-get update
RUN apt-get install -y openssh-server
# add a new user 'remote_user'
RUN useradd remote_user  && \
    echo "1234" | passwd remote_user && \
    mkdir /home/remote_user/..ssh && \
    chmod 700 /home/remote_user/.ssh
# copy ssh pub key
COPY remote-key.pub /home/remote_user/.ssh/authorized_keys

# make remote_user owner
RUN chown remote_user:remote_user -R /home/remote_user/.ssh/ && \
    chmod 600 /home/remote_user/.ssh/authorized_keys

# generate some keys needed for ssh
RUN /usr/sbin/sshd-keygen

# which command to be executed
CMD /usr/sbin/sshd -D

```
cd back to main folder: /jenkins-data

edit docker-compose file

```yaml
version: '3'

services:
  jenkins:
    container_name: jenkins
    image: jenkins/jenkins
    ports:
     - "8080:8080"
    volumes:
     - "$PWD/jenkins-home:/var/jenkins_home"
    networks:
     - net
  remote-host:
     container_name: remote-host
     image: remote-host
     # use custom dockerfile in dir 'debianos'

     build:
         context: debianos # this is where docker image file is located
     networks:
         - net
networks:
  net:

```
to remote into ssh server from jenkins container: ```ssh remote_user@remote-host```
to remote into ssh with key server from jenkins container: ```ssh -i remote_user@remote-host```

you can now use: "execute shell script on remote host using ssh" in jenkins job to run commands on remote-host

Video: https://bah.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12926008#overview

## <a name="dockeragents"></a>Jenkins Agents running in Docker container

### Setup of Agent
1. Install Docker plugin in Jenkins
2. Setup up Docker Cloud Details: Manage Node >  Configure Clouds > Docker Cloud Details
    - make sure **Expose daemon on tcp://localhost:2375 without TLS** is enabled on docker machine
    - enter ```tcp://host.docker.internal:2375``` for **Docker Host URI**
    - use "Test Connection"; you should see something like: ```Version = 19.03.8, API Version = 1.40```
    - check 'Enable' option and Save
3. Setup up Docker Agent Templates: Manage Node >  Configure Clouds > Docker Agent templates
    - Note: make sure you have image of slave: ```docker pull jenkins/slave```
        - https://hub.docker.com/r/jenkins/slave/
    - Labels: slave
    - check 'Enabled'
    - Name: Jenkins Slave'
    - docker image: jenkins/slave
    - Instance capcaity: 10
    - remote file system root: /home/jenkins/agent; obtained from docker image details
    - Save
### Run Job using Agent

1. Create a new job to run using new agent

```groovy
pipeline {
    agent {
        label 'slave'
    }

    stages {
        stage('Hello') {
            steps {
                sh 'java -version'
                echo 'Getting working dir...'
                sh 'pwd'
            }
        }
    }
}

```
https://bah.udemy.com/course/working-with-jenkins/learn/lecture/20959308?start=45#overview

## Catlight

Jenkins Build Monitor tool for developers

https://catlight.io/

## Integration with Ansible

- see guide: https://github.com/yankils/Simple-DevOps-Project/blob/master/Jenkins/Ansible_integration.MD
- video: https://bah.udemy.com/course/valaxy-devops/learn/lecture/15774634#overview
- https://bah.udemy.com/course/valaxy-devops/learn/lecture/15774666#overview

## Integration with Sonarqube

SonarQube continuously inspects your software project on code quality

https://www.sonarqube.org/

It can report on :
- bugs
- vulnerabilities (security issues)
- code smells (maintainability related issues)
- technical debt (estimated time required to fix)
- code coverage 

In Jenkins :
- code gets scanned by sonar-scanner
- sonar-scanner sends results to sonarqube server

Setup:
- sample docker compose file: https://github.com/wardviaene/jenkins-course/blob/master/docker-compose/docker-compose.yml
- see videos: https://bah.udemy.com/course/learn-devops-ci-cd-with-jenkins-using-pipelines-and-docker/learn/lecture/7237420#overview

## Useful plugins

- DSL - https://plugins.jenkins.io/job-dsl/
- Blue Ocean: https://jenkins.io/projects/blueocean/about/
- SSH - for ssh connections
- Deploy to Container: for deploying war file to a container after build
    - after installed this gives you option to choose this for your job: *Deploy war/ear to a container*
    - https://bah.udemy.com/course/valaxy-devops/learn/lecture/15776508#overview
- Publish Over SSH 
    - after install setup by going to : Jenkins > Configu > Publish Over SSH 
    - in your job use 'Send build artifacts over SSH' to send files to remote host (ex. Amazon EC2)
- HTTP Request plugin: https://www.jenkins.io/doc/pipeline/steps/http_request/

## Getting Plugins installed using Script Console

```http://<jenkins ip>/script```

use below code to output name and version of plugins:
```groovy

List<String> jenkinsPlugins = new ArrayList<String>(Jenkins.instance.pluginManager.plugins);
//println(jenkinsPlugins)
jenkinsPlugins.sort { it.displayName }
	.each {plugin ->
		println("${plugin.shortName}:${plugin.version}")
     }

```

## Webhooks
cdd
- [Automatically Trigger Jenkins Jobs Using Github WebHook](https://www.youtube.com/watch?v=adVWQc8T9qg)
# Resources
- Jenkins training repos: https://git
hub.com/jenkins-training
- containers - https://wiki.jenkins.io/display/JENKINS/Containers 
- groovy - https://www.eficode.com/blog/jenkins-groovy-tutorial
- [Configuring Content Security Policy ](https://www.jenkins.io/doc/book/system-administration/security/configuring-content-security-policy/)
    - Run this from Manage Jenkins > Script console: ```System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")```

Jenkins Overview

- https://www.lambdatest.com/blog/jenkins-pipeline-tutorial/
## Troubleshooting 

**Issue**: Processs get killed when job run is complete

**Solution**:
If running as windows service, edit *C:\Program Files (x86)\Jenkins\jenkins.xml* to add ```-Dhudson.util.ProcessTree.disable=true``` to the arguments


``` <arguments>-Xrs -Xmx256m -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle -Dhudson.util.ProcessTree.disable=true -jar "%BASE%\jenkins.war" --httpPort=8080 --webroot="%BASE%\war"</arguments>```

If running as war file, run as below:
```java -Dhudson.util.ProcessTree.disable=true -jar jenkins.war```

**Issue** Why is the option 'Launch agent by connecting it to the master' not available

**Solution**: [see link](https://support.cloudbees.com/hc/en-us/articles/360029791092-Why-is-the-option-Launch-agent-by-connecting-it-to-the-master-not-available)

Issue: error when trying to run dokcer compose: script.sh: docker-compose: not found

Fix: 
1. bash into container:  docker exec -it jenkins9000 bash
2. install docker-compose: [see guide](https://docs.docker.com/compose/install/)
    - ```sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```
    - ```sudo chmod +x /usr/local/bin/docker-compose```

sudo chmod +x /usr/local/bin/docker-compose