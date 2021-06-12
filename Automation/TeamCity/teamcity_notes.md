# Team City

[TeamCity](https://www.jetbrains.com/teamcity/) is a build management and continuous integration server from JetBrains similiar to Jenkins

- [TeamCity Documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html)

## Setup With Docker

- [Server docker image info](https://hub.docker.com/r/jetbrains/teamcity-server/)
- [Agen Docker Image](https://hub.docker.com/r/jetbrains/teamcity-agent)
- Run server command: ```docker run -it --name teamcity-server-instance -v <path-to-data-directory>:/data/teamcity_server/datadir -v <path-to-logs-directory>:/opt/teamcity/logs -p <port-on-host>:8111 jetbrains/teamcity-server```


## Server Setup
1. start TeamCity server as docker container: ```docker run -it --name teamcity-server-instance -v $PWD:/data/teamcity_server/datadir -v $PWD:/opt/teamcity/logs -p 8111:8111 -d jetbrains/teamcity-server```
2.  Access: ```http://192.168.1.25:8111```
3. follow prompts

## Agent setup

1. start TeamCity agent 
    - without docker volume mount in Linux: ```docker run -it -e SERVER_URL="192.168.1.25:8111"  -v $PWD:/data/teamcity_agent/conf  -d jetbrains/teamcity-agent```
    - start TeamCity agent with docker volume mount: ```docker run -e SERVER_URL="http://192.168.1.25:8111" -v team_city_agent_config_two:/data/teamcity_agent/conf  -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -d jetbrains/teamcity-agent```
    - [command example](https://gitlab.com/nanuchi/devops-tool-of-month/-/blob/master/teamcity/commands.md)
3. authorize agencys by going to Agents page on server: ```http://192.168.1.25:8111/agents.html```
## Notes

- you can setup connections to external sites (ex. docker hub) by going to ```ProjectName > Connections```
- under project > build configuration > DSL  you can generate infrastructure as code written in [Kotlin DSL](https://www.jetbrains.com/help/teamcity/kotlin-dsl.html). similiar to groovy script in Jenkins


## Video Tutorials

- [CI/CD with JetBrains TeamCity](https://www.youtube.com/watch?v=zqi4fDF-S60)
    