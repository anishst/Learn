# SonarQube

SonarQube is an automatic code review tool to detect bugs, vulnerabilities, and code smells in your code. It can integrate with your existing workflow to enable continuous code inspection across your project branches and pull requests.

## Docs

- [https://docs.sonarqube.org/latest/](https://docs.sonarqube.org/latest/)

## Server Setup Options
   1. direct install and configure locally
        - [Download](https://www.sonarqube.org/downloads/)
        - [Install Server Guide](https://docs.sonarqube.org/latest/setup/install-server/)
   2. Docker container (easier way)
       - [https://hub.docker.com/_/sonarqube](https://hub.docker.com/_/sonarqube)

## Sonar Scanner Setup
   - this will be installed locally on the machine with code
   - [Sonar scanner download](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)
   
    
## Docker Quick run

1. run: ```docker run -d --name sonarqube -p 9000:9000 sonarqube```
2. login with default admin:http://host_ipaddress:9000 
    - username = admin
    - pwd = admin
    
## Docker Compose Way

```yaml

version: "3"
 
services:
  sonarqube:
    image: sonarqube
    container_name: sonarqube
    restart: always
    environment:
      - SONARQUBE_JDBC_USERNAME=sonar
      - SONARQUBE_JDBC_PASSWORD=password1
      - SONARQUBE_JDBC_URL=jdbc:postgresql://db:5432/sonarqube
    ports:
      - "9000:9000"
      - "9092:9092"
    volumes:
      - sonarqube_conf:/opt/sonarqube/conf
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
      - sonarqube_bundled-plugins:/opt/sonarqube/lib/bundled-plugins
 
  db:
    image: postgres:10.1
    container_name: db
    restart: always
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=password1
      - POSTGRES_DB=sonarqube
    volumes:
      - sonarqube_db:/var/lib/postgresql
      - postgresql_data:/var/lib/postgresql/data
 
volumes:
  postgresql_data:
  sonarqube_bundled-plugins:
  sonarqube_conf:
  sonarqube_data:
  sonarqube_db:
  sonarqube_extensions:
```

1. create folder with yaml file above
2. run: ```docker-compose up -d```
    - on Linux system make sure to run this first: ```sysctl -w vm.max_map_count=262144```
3. login with default admin:http://host_ipaddress:9000
4. create a test project and token following prompts
5. go to source code directory and run the scan:
    - Example: ```sonar-scanner.bat -D"sonar.projectKey=test" -D"sonar.sources=." -D"sonar.host.url=http://192.168.1.25:9000" -D"sonar.login=0d8532420aa644b8d29cedbceca575557596e40c"```


## Video Guides

   - [Docker compose way With Java Code](https://www.youtube.com/watch?v=u5HMAu7Ocuk&t=144s) 