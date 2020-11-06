# Amazon Web Services (AWS)

- AWS was launched in 2006

Amazon Products: https://aws.amazon.com/products/

Service Summary - https://i.imgur.com/k013j1R.png


AWS Foundtions services
https://image.slidesharecdn.com/hsbcandawsday-awsfoundations-170709164032/95/hsbc-and-aws-day-aws-foundations-7-638.jpg?cb=1499618785

AWS Platform Services

https://image.slidesharecdn.com/getting-started-on-aws-awsome-19b96808-0f60-4c92-96f1-d7937c855042-304968793-180413164036/95/getting-started-on-aws-awsome-day-2018-12-638.jpg?cb=1523637675

## AWS Fundamentals: IAM & EC2

### IAM (Identity and Access Management )

- whole AWS security is here; users, groups, role
- root acct should never be used/shared
- IAM is global; across regions
- permissions are govered by poliies (JSON)
- mfa can be setup
- IAM Federation; for big enterprises
    - uses SAML Standard (AD)
- One IAM User per physicla person
- one IAM role per application
- never use ROOT accont except for initial setup


### AWS Management Console
 - use MFA - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html

 
### AMI - Amazon Machine Image
 - EC2 is based off AMI; similiar to docker image
 - OS + setup of software pre-installed
 - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html
 - use AMI TO pre-install software > faster boot
    - AMI is region based
    
### Setup

https://infrastructure.aws/

- regions
    - geo locations / isolated from each other
    - consist of at least 2 availablity zone
- availablity zones
    - clusters of data centers / min 2 AZ in a region
    - isolated from other zones
    - connecte by a low-latency link
    - edge locations host a CDN
    
https://aws.amazon.com/about-aws/global-infrastructure/

### Amazon EC2

- Virtual machines that provides resizable compute capacity in cloud
- Amazon EC2 Instance Types: https://aws.amazon.com/ec2/instance-types/
- https://docs.aws.amazon.com/ec2/index.html
- instance lifecycle: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html
    - charged while in rebooting and running state
 - metadata: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
 - Purchase options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html
 - EC2 Launch modes:
    - on-demand - pay as you go
    - reserved - 1-3 yr contract
    - dedicated - dedicated hardware; nonshared
    - spot - bidding unused instances
- billed by the second; t2.micro is free tier
- security groups can reference other security groups instead of IP ranges
- default user accounts: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html

#### Connection Options for EC2

Connect options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html

**SSH**

- create new key pair
- save PEM file
- edit Edit inbound rules to allow SSH (SSH /TCP / 25 / Anywhere)
- form a terminal window go to directly with PEM file and enter this command: ```ssh -i ec2_tutorial.pem ec2-user@ipaddress```
- on linux you might need give permissionS if get error "bad permissions" : ```chmod 400 file.pem```
- if you need to run commands as root: ```sudo su```
- if u need to upgrade: ```yum update -y```
- on windows make your the owner of the pem file; disable inheritance and make sure you only have accessa nd have full control
- Help: https://bah.udemy.com/course/selenium-webdriver-with-docker/learn/lecture/14317256#overview
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

Via browser using EC2 Instance connect

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

- Quick start: https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/welcome.html


### Sample script to setup a web server

below script can be used to test an EC2 instance; 

the script will:
- install apache (httpd)
- config web server to automatically start on boot
- activate web server
- create a simple web page
    ```shell script
    #!/bin/bash
    yum -y install httpd
    systemctl enable httpd
    systemctl start httpd
    echo "<html><body bgcolor=#D7EDF5><h1>Hello Anish! Welcome to your AWS Web Server $(hostname -f)!</h1></body></html>" > /var/www/html/index.html
    ```
Note: make to sure edit security group to allow HTTP access: Security Groups > web server security group > inbound rules tab > edit > add rule > type: HTTP Source: Anywhere > Save rules

### Getting log from EC2 instance

- Actions > Instance Settings > Get System Log

## Virtual Private Cloud (VPC)
 - for networking
 - users private cloud in a region
 - **Subnets**
    - logicl grouping of resources within the VPC
    - public subnet - can access from interent
    - private subnet
 - **Internet Gateway** connects VPC to internet
 - IPV4 CIDR 10.0.25.0/24 means the subnet contains ip addresses from 10.0.25.0 to 10.0.25.255
 - each subnet is assoicated with a **route table**, which specifies the routes for outbound traffic leaving the subnet
 - a **network acces control list (ACL)** is an optional layter of security for VPC; usually left with default values; act as firewall for controlling traiffc in/out of subnets
 - a **Network Address Translation (NAT) gateway** allows resources in a private subnet to connect to internet
- Guide: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- Security gropus compare: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html
- VPC Flow logs
    - capture ip traffic info
- VPC Peering
    - connect 2 VPCs privately using AWS network
    - not transitive 
- VPC Endpoints
    - allows you to connect to AWS services using private network 
    - VPC Endpoit gateway: give VPC access to S3, DynamoDB
- Site to Site VPN & Direct Connect

## Amazon DB Services: DB options
- self-managed
    - db server on EC2; Bring ur own license
- fully managed
    - amazon RDS / amazon aurora
    - Amazon dynamodb
    - amazon redshift


## High Availability and Scalability: ELB & ASG

- Vertical scalability 
    - increase size of instance; ex. t2.micro to t2.large
- horizontal scalability 
    - increase number of instances
    - common for web apps
- high availability
    - run in at least 2 data centers
    - goal is to survive data center loss

### ELB - Elastic Load Balancing

## Direct Connect

##  EC2 Storage - EBS & EFS

### EBS - Elastic Block Store
- network drive you can attach to your instance while they run
- locked to AZ 
- https://aws.amazon.com/ebs
- Making an Amazon EBS volume available for use on Linux - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

### EFS - Elastic File System
- network file system
- only linux based AMI

## Simple Storage Service(S3)
 
 - object storage and distribtuon for the internet
 - part of Amazon CloudFront
 - 99.999999 % durability
 - can be used to shift static content from web instances
 - storage classes
    - standard
    - standard - infrequent access
    - glacier
  - versioning: https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html

## AWS Athena

- serverless service to peroform anlayltic directly again S3 files
- uses SQL
- https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/

## AWS CloudFront

- Content delivery network (CDN)
- improves read performance, content is cahced at edge
- https://aws.amazon.com/cloudfront/features/    
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

## Amazon Elastic Container Service (ECS)
- https://aws.amazon.com/ecs/
- fully managed container orchestration service

## AWS Elastic Beanstalk
- easy-to-use service for deploying and scaling web applications and services
- platform as a service; managed service; developer responsible for code only
- beansstalk itself is free; pay for resources that make up app
- https://aws.amazon.com/elasticbeanstalk/
- deployment options: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html

## AWS CloudFormation

- infrastruce as code
- declarative way of outling your AWS infrastructure
-  


### Glacier

   - archving service

### Automation Tools
- AWS Elastic beanstalk - deoploy code to cluod
- opswork - mange infrastructure
- cloudformation - define infrastructure

#### Tools to record UI clicks:
- https://chrome.google.com/webstore/detail/console-recorder-for-aws/ganlhgooidfbijjidcpkeaohjnkeicba?hl=en
- console recorder: https://addons.mozilla.org/en-CA/firefox/addon/console-recorder/#:~:text=Extension%20Metadata&text=Click%20the%20orange%20Console%20Recorder,click%20the%20Start%20Recording%20button.


## Databases


- **Amazon RDS - RelationAL Database Service**
    - https://aws.amazon.com/rds/
    - managed DB by AWS
        - Postgress, MySQL, mariadb, oracle, ms sql, Aurora (aws db)
    - Automatic backup
    - DB snapshots - triggerd by user
    - RDS Read replicas for read scalability
        - up to 5; ASYNC replication
    - FREE-TIER Compatible
        - MySQL
        - Each calendar month, the free tier will allow you to use the Amazon RDS resources listed below for free:
            - 750 hrs of Amazon RDS in a Single-AZ db.t2.micro Instance.
            - 20 GB of General Purpose Storage (SSD).
            - 20 GB for automated backup storage and any user-initiated DB Snapshots.
    - you can use this tool to make queries: https://sqlectron.github.io/
    - you will need Endpoint and port found under: Connectivity & security in your DB instance in AWS.
    - RDS Security - encryption
        - at reset
        - in-flight
    - RDS - IAM Auth: no pwd needed; token lifetime of 15 mins

- **Amazon Aurora**
    - proprietary DB technology from AWS
    - Automatically grows; 10GB increments
    - up to 15 replicas

- **AWS ElaticCache**
    - in memory databases; Redis or MemCached
    - RDS for caches; relieves load on RDS
    - can store user sessions
        
- DynamoDB - NoSQL DB

## AWS CLI

https://aws.amazon.com/cli/

1. Log into aws: create Access keys (access key ID and secret access key)
2. go to command prompt: ```aws configure```, follow prompts
    - to see configs: ```~/.aws/credentials```
    - more info: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
3. you can test access by trying to connect to one of the services; 
    - example show all s3 buckets: ```aws s3 ls``` 
    - list files in bucket: ```aws s3 ls s3://anishbucket2020```
    - make a new bucket: ```aws s3 mb s3://testbyanish```
    - remove bucket: ```aws s3 rb s3://testbyanish```
    - and more: https://docs.aws.amazon.com/cli/latest/reference/s3/
    
- NEVER configure CLI access key in EC2 instance! use IAM user policy instead
- you can assign policy to EC2 instance to give the needed permissions
- EC2 Instance metadata
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
    - internal ip; http://169.254.169.254/latest/meta-data/
        - can get data about EC2 instances
- AWS CLI profile
    - ```aws configure --profile myotherawsacct```
    - to run a command using other: ```aws s3 ls --profile myotherawsacct```
- AWS CLI MFA
    - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_cliapi.html
    - https://docs.aws.amazon.com/cli/latest/reference/sts/get-session-token.html
- AWS SDK
    - perfomr actions on AWS directly from your app w/o using CLI
    -https://aws.amazon.com/tools/
    - AWS CLI uses Python SDK (boto3)
- AWS Limits (quotas)
    - API rate limits
    - service quota


## Compliance

- https://aws.amazon.com/compliance/
- https://aws.amazon.com/compliance/programs/
- https://aws.amazon.com/artifact/

## Encryption

https://aws.amazon.com/kms/

## Security
- AWS AWS Identity and Access Management (IAM)
- security groups
- network ACLs
- white paper: https://d1.awsstatic.com/whitepapers/aws-security-whitepaper.pdf
- Security, Identity, and Compliance: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-services.html
- Diagram : https://aws.amazon.com/compliance/shared-responsibility-model/
## Networking

## Resources
- Getting started: https://aws.amazon.com/getting-started/
- Free tier info: https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc
- Documentation: https://docs.aws.amazon.com/
- What's New with AWS? https://aws.amazon.com/new/?whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc
- Free Tier Monitoring: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html#free-budget
-  AWS Total Cost of Ownership (TCO) Calculators - https://aws.amazon.com/tco-calculator/
- new pricing: https://calculator.aws/#/
- simple monthly calculator: https://calculator.s3.amazonaws.com/index.html
- Shared Responsibility Model https://aws.amazon.com/compliance/shared-responsibility-model/
- workspaces (virtual desktop) https://aws.amazon.com/workspaces/

## Certifications

- https://aws.amazon.com/certification/

![Image](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2019/09/20/Certifications_1.png)
## Training
- https://www.aws.training/
- https://amazon.qwiklabs.com/catalog
- awesome day: https://aws.amazon.com/events/awsome-day/
- workshops: https://aws.amazon.com/serverless-workshops/