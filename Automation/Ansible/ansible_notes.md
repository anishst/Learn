# Ansible

Ansible is a radically simple IT automation system. It handles configuration management, application deployment, cloud provisioning, ad-hoc task execution, network automation, and multi-node orchestration. Ansible makes complex changes like zero-downtime rolling updates with load balancers easy. More information on the Ansible website.

https://github.com/ansible/ansible

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

## Components

 - control node - any machine with Ansible installed; manages client nodes
 - manged nodes - devices(servers) you manage with Ansible
 - inventory - info about nodes; also called hostfile
 - playbooks - actual tasks to run on nodes; ordered list of tasks
 - modules - used by tasks; units of code Ansible executes

## Setup

- cannot install control node on windows (linux only)

 
 
## Setup on CentOS

https://docs.docker.com/engine/install/centos/

1. switch to root user: ```sudo su -```
2. install python: ```yum install python or python3```
3. install ansible: ```pip3 install ansible```
4. check ansible version: ```ansible --version```
5. create ansible folder:  ```mkdir /etc/ansible```
6. create user: ```useradd ansadmin```
7. set pwd: ```passwd ansadminpwd```
5. add ansadmin to sudoers file: visudo
6. add this at end to skip from being prompted for pwd: ```ansadmin ALL=(ALL)   NOPASSWD: ALL```
7. install docker
8. start docker: service docker start
9. add ansadmin user to docker group: ```usermod -aG docker ansadmin```
10. if needed edit ssh config: 
    - vi /etc/ssh/sshd_config
    - check to make sure ```PasswordAuthentication yes``` is enabled and set to yes
    - reload ssh service: ```service sshd reload```
11. generate keys for ansamdin account
    - switch to:  ```su - ansadmin```
    - gen key: ```ssh-keygen``` follow prompts
    - cd .ssh
    - copy id_rsa.pub: ```ssh-copy-id ansadmin@<dockerhostip>```

### Playbook File example

example: playbook.yml
```yaml
---
- hosts: all # where to run
  become: true # run as root?
  tasks:
  - name: stop if we have old docker container
    command: docker stop simple-devops-container
    ignore_errors: yes

  - name: remove stopped docker container
    command: docker rm simple-devops-container
    ignore_errors: yes

  - name: remove current docker image
    command: docker rmi simple-devops-image
    ignore_errors: yes

  - name: building docker image
    command: docker build -t simple-devops-image .
    args:
      chdir: /opt/docker

  - name: creating docker image
    command: docker run -d --name simple-devops-container -p 8080:8080 simple-devops-image```
# source: https://github.com/yankils/Simple-DevOps-Project/blob/master/Jenkins_Jobs/simple-docker-project.yml

```
To execute playbook: ```ansible-playbook -i hosts <playbooky.yml> --check```

Video: https://bah.udemy.com/course/valaxy-devops/learn/lecture/15774652#overview

### Resources

- setup on amazon ec2: https://github.com/yankils/Simple-DevOps-Project/blob/master/Ansible/Ansible_installation.MD
