 # Amazon Web Services (AWS)

- AWS was launched in 2006

Amazon Products: https://aws.amazon.com/products/

Service Summary - https://i.imgur.com/k013j1R.png

- [Types of Cloud Computing](https://aws.amazon.com/types-of-cloud-computing/)
- serverless computing
    - no infrastructure, less management
    - automatical scaling
    - highly available and secure
    - pay for value


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
- Users can be assigned an access key ID and secret access key for programmatic access to the AWS API, CLI, SDK, and other development tools and a password for access to the management console.
- Access keys are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).
- Server certificates are **SSL/TLS certificates** that you can use to authenticate with some AWS services.

### AWS Management Console
 - use MFA - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html

 
### AMI - Amazon Machine Image
 - EC2 is based off AMI; similiar to docker image
 - OS + setup of software pre-installed
 - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html
 - use AMI TO pre-install software > faster boot
    - AMI is region based
    
### AWS Global Infrastructure

https://infrastructure.aws/

- regions
    - geo locations / isolated from each other
    - consist of at least 2 availablity zone
    - Data stored within an AWS region is not replicated outside of that region automatically
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
- availablity zones
    - clusters of data centers / min 2 AZ in a region
    - isolated from other zones
    - connecte by a low-latency link
    - edge locations host a CDN
- EC2 instance must have AMI in the same region; or copy over to new region    
    
https://aws.amazon.com/about-aws/global-infrastructure/

### Amazon EC2

- Virtual machines that provides resizable compute capacity in cloud
- Amazon EC2 Instance Types: https://aws.amazon.com/ec2/instance-types/
   - EC2 Dedicated Host
       - allows an organization to bring their own licensing on host hardware that is physically isolated from other AWS accounts
    
- https://docs.aws.amazon.com/ec2/index.html
- instance lifecycle: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html
    - charged while in rebooting and running state
 - metadata: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
 - Purchase options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html
 - EC2 Launch modes:
    - on-demand - pay as you go
    - reserved - 1 or 3 yr terms
        - Benfits
            - reserver capacity
            - [reduced cost](https://aws.amazon.com/ec2/pricing/reserved-instances/)
    - dedicated - dedicated hardware; nonshared
    - spot - bidding unused instances
    - launch instances within a VPC across multiple AZs. It cannot launch resources into another AWS Region.
- billed by the second; t2.micro is free tier
- security groups can reference other security groups instead of IP ranges
- default user accounts: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html
- pricing - https://aws.amazon.com/ec2/pricing/

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

    ```
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
- spans all the Availability Zones in the region
- VPC Flow logs
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
   - automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, Lambda functions, and virtual appliances.
   - https://aws.amazon.com/elasticloadbalancing 
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
  - replication 
    - S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions
  - Bucket policies are used for controlling access to buckets
  - Lifecycle management 
    - create rules to control the transfer of objects between different storage classes
    - https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html
## Amazon EMR

- big data
- process vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto.
 
## AWS Storage Gateway
- **hybrid cloud storage** service that gives you **on-premises** access to virtually unlimited cloud storage
- three different types of gateways 
    - File Gateway
        - Store and access objects in Amazon S3 from NFS or SMB file-based applications with local caching
    - Tape Gateway
        - Backup and archive on-premises data to virtual tapes in AWS
    - Volume Gateway 
        - Hybrid cloud block storage with local caching
    
## AWS Athena

- serverless service to peroform anlayltic directly again S3 files
- uses SQL
- https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/

## Route 53

- https://aws.amazon.com/route53/
- services
    - DNS
    - Traffic flow
    - domain registration
    - routing policies (not IP routing)
## AWS CloudFront

- Content delivery network (CDN)
- improves read performance, content is cahced at edge
- https://aws.amazon.com/cloudfront/features/    
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

## Amazon Elastic Container Service (ECS)
- https://aws.amazon.com/ecs/
- fully managed container orchestration service

## AWS CloudFormation

- infrastruce as code
- declarative way of outling your AWS infrastructure using YAML/JSON; YAML is better for CF
-  AWS CloudFormation template formats - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html
- [stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
- AWS TaskCat
    - tests cloudformation templates
- Template examples: https://aws.amazon.com/cloudformation/resources/templates/

stack launch example

```aws cloudformation create-stack --stack-name AWSStudent-Lab1 --template-body file://[simple-infrastructure-file-name] --parameters ParameterKey=KeyName,ParameterValue=[paste KeyPair name here] ParameterKey=InstanceType,ParameterValue=t2.micro```

Get info on stack

```aws cloudformation describe-stacks --stack-name AWSStudent-Lab1```

Delete stack

```aws cloudformation delete-stack --stack-name AWSStudent-Lab1```

Drift detection to identify resourced modifed outside AWS CloudFormation manageent

```aws cloudformation detect-stack-drift --stack-name AWSStudent-Lab1```

create change set

```aws cloudformation create-change-set --stack-name AWSStudent-Lab1 --change-set-name Lab1ChangeSet --template-body file://simple-infrastructure-CS.yaml --parameters ParameterKey=KeyName,ParameterValue=qwikLABS-L3644-5438 ParameterKey=InstanceType,ParameterValue=t2.micro```
execute change set

```aws cloudformation execute-change-set --stack-name AWSStudent-Lab1 --change-set-name Lab1ChangeSet```

## AWS Elastic Beanstalk
- easy-to-use service for deploying and scaling web applications and services
- uses Cloud Formation in backend
- platform as a service; managed service; developer responsible for code only
- beansstalk itself is free; pay for resources that make up app
- Beanstalk lifecycle policy
    - beanstak can store 1000 application versions
- Elastic Beanstalk - Single  Docker; not ECS uses EC2
- https://aws.amazon.com/elasticbeanstalk/
- deployment options: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html
- [Tutorials](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html)


## AWS Monitoring and Audit

### [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

- monitors applications  in real time. 
- collect and track metrics
- allows billing alarms
-  performs **app performance** monitoring and can monitor custom metrics generated by applications and the **operational health** of your AWS resources
### X-Ray

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. 

https://aws.amazon.com/xray/

## AWS Web Application Firewall (WAF) 
- protect web applications or APIs against common web exploits. Rules can be created that block traffic based on source IP address.
 
### CloudTrail

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. 
https://aws.amazon.com/cloudtrail/
- used for logging who does what in AWS by recording API calls. It is used for auditing, not performance or system operational monitoring.

## AWS Lambda

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.
https://aws.amazon.com/lambda/

- serverless event-driven code execution
- 15 min run time
- scales automatically
- monitor/log using CloudWatch

## AWS ECS

- fully managed container orchestration service

[https://aws.amazon.com/ecs/](https://aws.amazon.com/ecs/)

## AWS ECR

Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy your container images and artifacts anywhere

[https://aws.amazon.com/ecr/](https://aws.amazon.com/ecr/)

- amazon version of Docker Hub
## AWS EKS

Amazon Elastic Kubernetes Service (Amazon EKS) gives you the flexibility to start, run, and scale Kubernetes applications in the AWS cloud or on-premises.

[https://aws.amazon.com/eks/](https://aws.amazon.com/eks/)

## AWS Fargate

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). 

[https://aws.amazon.com/fargate/?nc=sn&loc=1](https://aws.amazon.com/fargate/?nc=sn&loc=1)

## DynamoDB 

- NoSQL serverless DB
- fully managed by AWS w/ replication across 3 AZ
- Made of tables; 
- Amazon DynamoDB Accelerator (DAX) 
    - provides in-memory acceleration to tables that result in significant performance improvements

https://aws.amazon.com/dynamodb/

## Reservations
   - Amazon ElastiCache and Amazon Redshift 

##  Glacier

   - archving service
   - data access
        - expedited: 1-5 mins
        - standard 3-5 hours
        - bulk; 5-12 hours
        - https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-two-steps.html

## Amazon Elasticsearch 
- Service is involved with operational analytics such as application monitoring, log analytics and clickstream analytics. 
   
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
        


## AWS CLI

- [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

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
- AWS SAM CLI
    - for serverless only
- AWS Cloud Dev Kit (AWS CDK)  
    - [aws cdk constructs](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html)
- AWS Limits (quotas)
    - API rate limits
    - service quota
- commands
    - ```aws ?``` - shows services
    - ```aws configure get region``` - show my region
    - ```aws ec2 describe-instances``` - show instance details
    - ```aws ec2 wait instance-running ...``` - use wait to add wait for ec2 to get loaded
    - ```aws ec2 describe-key-pairs``` - get key pair name
    - query language for JSON - https://jmespath.org/

## Security & Compliance

- https://aws.amazon.com/compliance/
- https://aws.amazon.com/compliance/programs/
- https://aws.amazon.com/artifact/

## AWS Cloud9

- free shared IDE using browser; real time; direct terminal access
- option to run: ec2 + aws cloud9 OR your server + aws cloud9
- for versioing use AWS codecommit or other remote rep (GitHub, etc)
- [https://aws.amazon.com/cloud9/](https://aws.amazon.com/cloud9/)

## AWS CodeStar

[https://aws.amazon.com/codestar/](https://aws.amazon.com/codestar/)

## AWS Step Functions 
 - lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. 

## AWS CodeCommit

fully-managed source control service that hosts secure Git-based repositories.

- free; backed by S3
- [https://aws.amazon.com/codecommit/](https://aws.amazon.com/codecommit/)
- [Setup](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html)

## AWS CodeBuild

fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. 

[https://aws.amazon.com/codebuild/](https://aws.amazon.com/codebuild/)

- No build servers to manage
- Monitor build throught CloudWatch events
- alternative to Jenkins, Bamboo, TeamCity, [AWS QuickStart](https://aws.amazon.com/quickstart)
- [Build Spec YAML File](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)

## AWS CodeDeploy 

CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.

- You can deploy a nearly unlimited variety of application content, such as code, web and configuration files, executable files, packages, scripts, multimedia files, and so on. 
- deploy application content stored in Amazon Simple Storage Service (Amazon S3) buckets, GitHub repositories, or Bitbucket repositories. You do not need to make changes to your existing code before you can use CodeDeploy. 
- rapidly release new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications, without many of the risks associated with error-prone manual deployments.
- [AppSpec config file YAML](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)
- [blue/green deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html#welcome-deployment-overview-blue-green)
- lifecycle hooks
- [Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

### Sample steps:

1. get code files: ```wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-DEVOPS/v3.0.9/lab-2-CodeDeploy/bundles/CodeDeployHeartbeatDemo.zip -P CodeDeployHeartbeatDemo```
2. create bucket: ```aws s3 mb s3://heartbeat-codedeploy-artifacts-ats-22043```
3. Deploy code to s3: ```aws deploy push --application-name CodeDeploy-Demo --source HeartBeat-App --s3-location s3://heartbeat-codedeploy-artifacts-ats-22043/HeartBeat-App.zip```
4. create deployment and push to s3 bucket: ```aws deploy create-deployment --application-name CodeDeploy-Demo --deployment-group-name HeartBeat-Deployment --deployment-config-name CodeDeployDefault.AllAtOnce --description "Initial Deployment" --s3-location bucket=heartbeat-codedeploy-artifacts-ats-22043,key=HeartBeat-App.zip,bundleType=zip```

## AWS CodePipeline

- fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. 
- CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define. This enables you to rapidly and reliably deliver features and updates. You can easily integrate AWS CodePipeline with third-party services such as GitHub or with your own custom plugin. With AWS CodePipeline, you pay for only what you use. There are no upfront fees or long-term commitments.
- [Docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
- [Actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions.html)
    - parallel/sequential/manual approvals

## AWS Security, Identity, & Compliance services

- [Overview](https://aws.amazon.com/products/security/)

### Encryption

https://aws.amazon.com/kms/

###  Security
- AWS AWS Identity and Access Management (IAM)
- security groups
- network ACLs
- white paper: https://d1.awsstatic.com/whitepapers/aws-security-whitepaper.pdf
- Security, Identity, and Compliance: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-services.html
- Diagram : https://aws.amazon.com/compliance/shared-responsibility-model/

### Amazon Macie

 Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS. Macie automatically provides an inventory of Amazon S3 buckets including a list of unencrypted buckets, publicly accessible buckets, and buckets shared with AWS accounts outside those you have defined in AWS Organizations. Then, Macie applies machine learning and pattern matching techniques to the buckets you select to identify and alert you to sensitive data, such as personally identifiable information (PII).

## Amazon Guard​Duty

- threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data stored in Amazon S3. 

### AWS Secrets Manager
AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets with a call to Secrets Manager APIs, eliminating the need to hardcode sensitive information in plain text. It cannot be used to discover and protect your sensitive data in AWS.

## AWS Organizations

- https://aws.amazon.com/organizations/
- centrally manage and govern your environment as you grow and scale your AWS resources
- Automate the creation of AWS accounts and categorize workloads using groups

### Consoldate billing

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html


## Networking

## AWS Well-Architected Framework


The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected) is based on five pillars: 

- Operational Excellence
- Security
- [Reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html)
- [Performance Efficiency](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/design-principles.html)
- Cost Optimization.

## Serverless

Serverless is the native architecture of the cloud that enables you to shift more of your operational responsibilities to AWS, increasing your agility and innovation. Serverless allows you to build and run applications and services without thinking about servers. It eliminates infrastructure management tasks such as server or cluster provisioning, patching, operating system maintenance, and capacity provisioning.

https://aws.amazon.com/serverless/

## Shared Responsibility Model 

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates.

- AWS is responsible for Security "of" the Cloud 
- For a service like Amazon EC2, that falls under Infrastructure as a Service, AWS is responsible for maintaining guest operating system 
- Configuration Management is the responsibility of the customer 
- AWS is responsible for training AWS and customer employees on AWS products and services
- https://aws.amazon.com/compliance/shared-responsibility-model/


### AWS Acceptable Use Policy

The Acceptable Use Policy describes prohibited uses of the web services offered by Amazon Web Services, Inc. and its affiliates (the “Services”) and the website located at http://aws.amazon.com (the “AWS Site”). This policy is present at https://aws.amazon.com/aup/ and is updated on a need basis by AWS.

https://aws.amazon.com/aup/


## Migration
- AWS Migration Hub
- AWS Database Migration Service
- AWS Server Migration Service

## AWS Support

###  Support Plans
- [Support Plans](https://aws.amazon.com/premiumsupport/plans/)
- All support plans provide 24×7 access to customer service, documentation, whitepapers, and support forums.
- Basic – billing and account support only (access to forums only).
- Developer – business hours support via email.
- Business – 24×7 email, chat and phone support.
- Enterprise – 24×7 email, chat and phone support.
    - TAM
        - Technical Account Manager provides expert monitoring and optimization for your environment and coordinates access to other programs and experts.
- AWS Concierge
    - support AWS customers on an Enterprise support plan with account issues
- APN Consulting Partners 
    - help an organization to design, build, and manage their workloads on AWS
    - 
### AWS Trusted Advisor

- Trusted Advisor is an online resource that helps to reduce cost, increase performance and improve security by optimizing your AWS environment.
- Trusted Advisor provides real time guidance to help you provision your resources following best practices.
- Advisor will advise you on Cost Optimization, Performance, Security, and Fault Tolerance.

- scans your AWS infrastructure and compares is to AWS best practices in five categories:
    - Cost Optimization
    - Performance
    - Security
    - Fault Tolerance
    - Service Limits
- https://aws.amazon.com/premiumsupport/technology/trusted-advisor/

### AWS Inspector 
- automated security assessment service that helps improve the security and compliance of applications deployed on AWS

### AWS Personal Health Dashboard

- provides alerts and remediation guidance when AWS is experiencing events that may impact you.

## AWS Systems Manager
- gives you visibility and control of your infrastructure on AWS. 
- provides a unified user interface so you can view operational data from multiple AWS services and **allows you to automate operational tasks** across your AWS resources.

## AWS OpsWorks
- configuration management service that provides managed instances of Chef and Puppet.

## AWS Glue
- serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.

## Amazon Neptune
- a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. 

## AWS Snowball 
suitcase-sized data migration and edge computing device that comes in two device options: Compute Optimized and Storage Optimized. Snowball Edge Storage Optimized devices provide 40 vCPUs of compute capacity coupled with 80 terabytes of usable block or Amazon S3-compatible object storage. 
-  move up to 80TB per device. AWS call this a “petabyte-scale data transfer service”.

## AWS Snowmobile
- move 100PB per snowmobile. AWS call this an “Exabyte-scale data transfer service”.
- **shipping container**  moved with a tractor-trailer. These services can assist with data migration, disaster recovery, data center shutdown, and remote data collection projects.

## AWS Config 
- fully-managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and regulatory compliance.

## AWS Artifact 
- central resource for compliance-related information. This service can be used to get compliance information related to AWS’ certifications/attestations.
## Resources

- Getting started: https://aws.amazon.com/getting-started/
- [Hands-On](https://aws.amazon.com/getting-started/hands-on/)
- [Break a Monolith Application into Microservices ](https://aws.amazon.com/getting-started/hands-on/break-monolith-app-microservices-ecs-docker-ec2/)
- [Free tier info](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)
- Documentation: https://docs.aws.amazon.com/
- What's New with AWS? https://aws.amazon.com/new/?whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc
- Free Tier Monitoring: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html#free-budget
-  AWS Total Cost of Ownership (TCO) Calculators - https://aws.amazon.com/tco-calculator/
- new pricing: https://calculator.aws/#/
- simple monthly calculator: https://calculator.s3.amazonaws.com/index.html
- six advantages of cloud computing: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html

- workspaces (virtual desktop) https://aws.amazon.com/workspaces/

## Certifications

- https://aws.amazon.com/certification/
- [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf)
- [examp prep cheat sheets](https://digitalcloud.training/certification-training/aws-certified-cloud-practitioner)

![Image](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2019/09/20/Certifications_1.png)
## Training
- https://www.aws.training/
- https://amazon.qwiklabs.com/catalog
- awesome day: https://aws.amazon.com/events/awsome-day/
- workshops: https://aws.amazon.com/serverless-workshops/

## DevOps on AWS

- [Deployment Strategies](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html)
- [CD](https://aws.amazon.com/devops/continuous-delivery/)
 - [Working with deployment configurations in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
 - [Testing](https://aws.amazon.com/blogs/devops/tag/testing/)
 - [DevSecOps](https://aws.amazon.com/blogs/security/tag/devsecops/)
    - [Definition](https://www.ibm.com/cloud/learn/devsecops)