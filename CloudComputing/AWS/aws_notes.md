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

## AWS CloudFormation

- infrastruce as code
- declarative way of outling your AWS infrastructure using YAML/JSON; YAML is better for CF
-  AWS CloudFormation template formats - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html
- [stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
- AWS TaskCat
    - tests cloudformation templates
- Template examples: https://aws.amazon.com/cloudformation/resources/templates/
```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  AWS CloudFormation Simple Infrastructure Template
  VPC_Single_Instance_In_Subnet: This template will show how to create a VPC and
  add an EC2 instance with an Elastic IP address and a security group.
Parameters:
  VPCCIDR:
    Description: CIDR Block for VPC
    Type: String
    Default: 10.199.0.0/16
    AllowedValues:
      - 10.199.0.0/16
  PUBSUBNET1:
    Description: Public Subnet 1
    Type: String
    Default: 10.199.10.0/24
    AllowedValues:
      - 10.199.10.0/24
  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    Default: t2.nano
    AllowedValues:
      - t2.nano
      - t2.micro
      - t2.small
    ConstraintDescription: must be a valid EC2 instance type.
  KeyName:
    Description: Keyname for the keypair that Qwiklab will use to launch EC2 instances
    Type: 'AWS::EC2::KeyPair::KeyName'
    ConstraintDescription: must be the name of the provided existing EC2 KeyPair.
  SSHLocation:
    Description: ' The IP address range that can be used to SSH to the EC2 instances'
    Type: String
    MinLength: '9'
    MaxLength: '18'
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
  LatestAmiId:
    Description: Find the current AMI ID using System Manager Parameter Store
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
  QwiklabLocale:
    Default: en
    Description: >-
      The locale of the student will be passed in to this parameter via the
      Qwiklab platform (via the student's browser)
    Type: String
Resources:
  VPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: !Ref VPCCIDR
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
        - Key: Name
          Value: CF lab environment
  Subnet:
    Type: 'AWS::EC2::Subnet'
    DependsOn: VPC
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PUBSUBNET1
      MapPublicIpOnLaunch: 'true'
      AvailabilityZone: !Select 
        - '0'
        - !GetAZs ''
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
        - Key: Name
          Value: Public Subnet
  InternetGateway:
    Type: 'AWS::EC2::InternetGateway'
    DependsOn: VPC
    Properties:
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
  AttachGateway:
    Type: 'AWS::EC2::VPCGatewayAttachment'
    DependsOn: VPC
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
  RouteTable:
    Type: 'AWS::EC2::RouteTable'
    DependsOn: VPC
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
  Route:
    Type: 'AWS::EC2::Route'
    DependsOn:
      - VPC
      - AttachGateway
    Properties:
      RouteTableId: !Ref RouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
  SubnetRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      SubnetId: !Ref Subnet
      RouteTableId: !Ref RouteTable
  NetworkAcl:
    Type: 'AWS::EC2::NetworkAcl'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
  InboundHTTPNetworkAclEntry:
    Type: 'AWS::EC2::NetworkAclEntry'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      NetworkAclId: !Ref NetworkAcl
      RuleNumber: '100'
      Protocol: '6'
      RuleAction: allow
      Egress: 'false'
      CidrBlock: 0.0.0.0/0
      PortRange:
        From: '80'
        To: '80'
  InboundSSHNetworkAclEntry:
    Type: 'AWS::EC2::NetworkAclEntry'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      NetworkAclId: !Ref NetworkAcl
      RuleNumber: '101'
      Protocol: '6'
      RuleAction: allow
      Egress: 'false'
      CidrBlock: 0.0.0.0/0
      PortRange:
        From: '22'
        To: '22'
  InboundResponsePortsNetworkAclEntry:
    Type: 'AWS::EC2::NetworkAclEntry'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      NetworkAclId: !Ref NetworkAcl
      RuleNumber: '102'
      Protocol: '6'
      RuleAction: allow
      Egress: 'false'
      CidrBlock: 0.0.0.0/0
      PortRange:
        From: '1024'
        To: '65535'
  OutBoundHTTPNetworkAclEntry:
    Type: 'AWS::EC2::NetworkAclEntry'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      NetworkAclId: !Ref NetworkAcl
      RuleNumber: '100'
      Protocol: '6'
      RuleAction: allow
      Egress: 'true'
      CidrBlock: 0.0.0.0/0
      PortRange:
        From: '80'
        To: '80'
  OutBoundHTTPSNetworkAclEntry:
    Type: 'AWS::EC2::NetworkAclEntry'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      NetworkAclId: !Ref NetworkAcl
      RuleNumber: '101'
      Protocol: '6'
      RuleAction: allow
      Egress: 'true'
      CidrBlock: 0.0.0.0/0
      PortRange:
        From: '443'
        To: '443'
  OutBoundResponsePortsNetworkAclEntry:
    Type: 'AWS::EC2::NetworkAclEntry'
    DependsOn:
      - VPC
      - InternetGateway
    Properties:
      NetworkAclId: !Ref NetworkAcl
      RuleNumber: '102'
      Protocol: '6'
      RuleAction: allow
      Egress: 'true'
      CidrBlock: 0.0.0.0/0
      PortRange:
        From: '1024'
        To: '65535'
  SubnetNetworkAclAssociation:
    Type: 'AWS::EC2::SubnetNetworkAclAssociation'
    Properties:
      SubnetId: !Ref Subnet
      NetworkAclId: !Ref NetworkAcl
  IPAddress:
    Type: 'AWS::EC2::EIP'
    DependsOn: AttachGateway
    Properties:
      Domain: vpc
      InstanceId: !Ref WebServerInstance
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      VpcId: !Ref VPC
      GroupDescription: Enable SSH access via port 22 and HTTP via port 80
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: !Ref SSHLocation
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          CidrIp: 0.0.0.0/0
  WebServerInstance:
    Type: 'AWS::EC2::Instance'
    DependsOn: AttachGateway
    Metadata:
      Comment: Install a simple application
      'AWS::CloudFormation::Init':
        config:
          packages:
            yum:
              httpd: []
          files:
            /var/www/html/index.html:
              content: !Join 
                - |+

                - - >-
                    <h1>Congratulations, you have successfully deployed a simple
                    infrastructure using AWS CloudFormation.</h1>
              mode: '000644'
              owner: root
              group: root
            /etc/cfn/cfn-hup.conf:
              content: !Join 
                - ''
                - - |
                    [main]
                  - stack=
                  - !Ref 'AWS::StackId'
                  - |+

                  - region=
                  - !Ref 'AWS::Region'
                  - |+

              mode: '000400'
              owner: root
              group: root
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Join 
                - ''
                - - |
                    [cfn-auto-reloader-hook]
                  - |
                    triggers=post.update
                  - >
                    path=Resources.WebServerInstance.Metadata.AWS::CloudFormation::Init
                  - 'action=/opt/aws/bin/cfn-init -v '
                  - '         --stack '
                  - !Ref 'AWS::StackName'
                  - '         --resource WebServerInstance '
                  - '         --region '
                  - !Ref 'AWS::Region'
                  - |+

                  - |
                    runas=root
              mode: '000400'
              owner: root
              group: root
          services:
            sysvinit:
              httpd:
                enabled: 'true'
                ensureRunning: 'true'
              cfn-hup:
                enabled: 'true'
                ensureRunning: 'true'
                files:
                  - /etc/cfn/cfn-hup.conf
                  - /etc/cfn/hooks.d/cfn-auto-reloader.conf
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: !Ref LatestAmiId
      KeyName: !Ref KeyName
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
        - Key: Name
          Value: Lab Host
      NetworkInterfaces:
        - GroupSet:
            - !Ref InstanceSecurityGroup
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: !Ref Subnet
      UserData: !Base64 
        'Fn::Join':
          - ''
          - - |
              #!/bin/bash -xe
            - |
              yum update -y aws-cfn-bootstrap
            - '/opt/aws/bin/cfn-init -v '
            - '         --stack '
            - !Ref 'AWS::StackName'
            - '         --resource WebServerInstance '
            - '         --region '
            - !Ref 'AWS::Region'
            - |+

            - '/opt/aws/bin/cfn-signal -e $? '
            - '         --stack '
            - !Ref 'AWS::StackName'
            - '         --resource WebServerInstance '
            - '         --region '
            - !Ref 'AWS::Region'
            - |+

    CreationPolicy:
      ResourceSignal:
        Timeout: PT15M
Outputs:
  URL:
    Value: !Join 
      - ''
      - - 'http://'
        - !GetAtt 
          - WebServerInstance
          - PublicIp
    Description: Newly created application URL

```  

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

### CloudWatch

Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications; https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html

### X-Ray

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. 

https://aws.amazon.com/xray/

### CloudTrail

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. 
https://aws.amazon.com/cloudtrail/

## AWS Lambda

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.

https://aws.amazon.com/lambda/

- serverless

## DynamoDB 

- NoSQL serverless DB
- fully managed by AWS w/ replication across 3 AZ
- Made of tables; 

https://aws.amazon.com/dynamodb/

##  Glacier

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

## AWS CodeCommit

fully-managed source control service that hosts secure Git-based repositories.

- free; backed by S3
- [https://aws.amazon.com/codecommit/](https://aws.amazon.com/codecommit/)
- [Setup](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html)

## AWS CodeBuild

fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. 

[https://aws.amazon.com/codebuild/](https://aws.amazon.com/codebuild/)

 - alternative to Jenkins, Bamboo, TeamCity
 - [Build Spec YAML File](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)
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

### AWS Secrets Manager
AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets with a call to Secrets Manager APIs, eliminating the need to hardcode sensitive information in plain text. It cannot be used to discover and protect your sensitive data in AWS.

## Networking

## AWS Well-Architected Framework

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. By using the Framework you will learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud. It provides a way for you to consistently measure your architectures against best practices and identify areas for improvement.

The AWS Well-Architected Framework is based on five pillars — Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization.

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

### AWS Trusted Advisor

AWS Trusted Advisor is an online tool that provides you real-time guidance to help you provision your resources following AWS best practices on cost optimization, security, fault tolerance, service limits, and performance improvement. Whether establishing new workflows, developing applications, or as part of ongoing improvement, recommendations provided by Trusted Advisor regularly help keep your solutions provisioned optimally. Trusted Advisor does not describe prohibited uses of the web services offered by Amazon Web Services.

## Resources
- Getting started: https://aws.amazon.com/getting-started/
- Free tier info: https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc
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

![Image](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2019/09/20/Certifications_1.png)
## Training
- https://www.aws.training/
- https://amazon.qwiklabs.com/catalog
- awesome day: https://aws.amazon.com/events/awsome-day/
- workshops: https://aws.amazon.com/serverless-workshops/

## AWS DevOps

