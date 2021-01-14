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

## Cloud Computing

### Deployment models

- cloud-based
- on premises
    - private cloud deployment.
- hybrid

### Advantages of cloud computing

- Trade upfront expense for variable expense.
- Benefit from massive economies of scale.
- Stop guessing capacity.
- Increase speed and agility.
- Stop spending money running and maintaining data centers.
- Go global in minutes.
- terms
    - capital expenses (capex)
    - operating expenses (opex).
    
### AWS Well-Architected Framework


The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected) is based on five pillars: 

- **Operational Excellence**
    - ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.
    - ability to run workloads effectively and gain insights into their operations
- **Security**
    - data integrity/encryption
    - There are six design principles for security in the cloud:
        – Implement a strong identity foundation
        – Enable traceability
        – Apply security at all layers
        – Automate security best practices
        – Protect data in transit and at rest
        – Prepare for security events
 - [**Reliability**](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html)
    - Recover from infrastructure or service disruptions
    - Dynamically acquire computing resources to meet demand
    - Mitigate disruptions such as misconfigurations or transient network issues
    - focuses on the ability of a workload to consistently and correctly perform its intended functions
    - five design principles for reliability in the cloud:
        - Test recovery procedures
        - Automatically recover from failure
        - Scale horizontally to increase aggregate system availability
        - Stop guessing capacity
– Manage change in automation.
- [**Performance Efficiency**](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/design-principles.html)
    - focuses on using computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve.
        - ex. using right EC2 instances
    - There are five design principles for performance efficiency in the cloud
        – Democratize advanced technologies
        – Go global in minutes
        – Use serverless architectures
        – Experiment more often
        – Mechanical sympathy.        
- **Cost Optimization**
    - control where money is spent
    - ability to run systems to deliver business value at the lowest price point.
    - five design principles for cost optimization in the cloud
        – Adopt a consumption model
        – Measure overall efficiency
        – Stop spending money on data center operations
        – Analyze and attribute expenditure
        – Use managed services to reduce cost of ownership

## Compute

### AMI - Amazon Machine Image
 - EC2 is based off AMI; similiar to docker image
 - OS + setup of software pre-installed
 - Amazon Machine Images (AMIs) can be used to quickly launch replacement instances when there is a failure
 - You must use an AMI from the same region as that of the EC2 instance. The region of the AMI has no bearing on the performance of the EC2 instance
 - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html
 - use AMI TO pre-install software > faster boot
    - AMI is region based
    
### AWS Global Infrastructure

https://infrastructure.aws/

- regions
    - geo locations / isolated from each other
    - consist of at least 2 availablity zone
    - Data stored within an AWS region is not replicated outside unless you configure it
    - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
    - factors affecting region selection
        - Compliance with data governance and legal requirements
        - Proximity to your customers
        - Available services within a Region
        - Pricing
- availablity zones
    - clusters of data centers / min 2 AZ in a region
    - isolated from other zones
    - connecte by a low-latency link
    - edge locations host a CDN
    - best practice is to run applications across at least two Availability Zones in a Region.
 - **Edge locations**
    - site that Amazon CloudFront uses to store cached copies of your content closer to your customers for faster delivery.
    - **AWS CloudFront**
        - AWS Content delivery network (CDN)
        - improves read performance, content is cahced at edge
        - https://aws.amazon.com/cloudfront/features/    
        - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
    - **Route 53**
        - https://aws.amazon.com/route53/
        - services
            - DNS
            - Traffic flow
            - domain registration
            - routing policies (not IP routing)
        - Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources.
- **AWS Outposts**      
    - service that enables you to run infrastructure in a hybrid cloud approach
    - Extends AWS infrastructure and services to your on-premises data center.

- EC2 instance must have AMI in the same region; or copy over to new region    
    
https://aws.amazon.com/about-aws/global-infrastructure/

### Amazon EC2 (Elastic Compute Cloud)

- Virtual machines that provides resizable compute capacity in cloud
- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
    - Compute optimized instances
    - Memory optimized instances
    - Accelerated computing instances
    - Storage optimized instance
- EC2 Dedicated Host
       - allows an organization to bring their own licensing on host hardware that is physically isolated from other AWS accounts
       - meet per-core license requirements
- https://docs.aws.amazon.com/ec2/index.html
- instance lifecycle: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html
    - charged while in rebooting and running state
 - metadata: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
 - [tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
    - separate cost for AWS services by the department for cost allocation
    - assign metadata to your AWS resources in the form of tags. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. You can create tags to categorize resources by purpose, owner, environment, or other criteria.
 - [Purchase options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)
    - on-demand
    - saving-plans
    - reservered instances
        - 1 or 3 yr terms
        - Reserved Instances (RIs) provide you with a significant discount (up to 72%) compared to On-Demand instance pricing. Standard reserved instances offer the most cost savings. RIs are based on a 1 or 3 year contract so they are suitable for workloads that will run for the duration of the contract period.
        - https://aws.amazon.com/ec2/pricing/reserved-instances/
        - **Standard RIs**: These provide the most significant discount (up to 75% off On-Demand) and are best suited for steady-state usage.
        - **Convertible RIs**: These provide a discount (up to 54% off On-Demand) and the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value. Like Standard RIs, Convertible RIs are best suited for steady-state usage.
        - **Scheduled RIs**: These are available to launch within the time windows you reserve. This option allows you to match your capacity reservation to a predictable recurring schedule that only requires a fraction of a day, a week, or a month.
    - spot instances
        - 2 min warning before terminated
    - dedicated hosts
        - physical machines
- billing
  - Amazon EC2 instances running Linux are billed in one second increments, with a **minimum of 60 seconds**
    - [https://aws.amazon.com/blogs/aws/new-per-second-billing-for-ec2-instances-and-ebs-volumes/](https://aws.amazon.com/blogs/aws/new-per-second-billing-for-ec2-instances-and-ebs-volumes/)
  - by hour for non-ec2 instance types 
  - Reserved and Spot Amazon EC2 Linux instances are charged per second with a minimum charge of 1 minute.
  - Use the AWS Simple Monthly Calculator to accurately model multitiered application stack
pricing.
  - Use the AWS Total Cost of Ownership Calculator to compare on-premises with AWS
deployment costs.
        
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
- benefits of using reserved instances
    - https://aws.amazon.com/ec2/pricing/reserved-instances/
    - reduced cost
    - reserver capcaicty

### Lighsail
- service that is used for running virtual instances and databases using a simplified user interface for users who are less experienced with AWS (also at a much lower cost than EC2).    

## Networking

### Connectivity to AWS
- **Virtual Private Cloud (VPC)**
    - for networking; establish boundaries around your AWS Resource
    - spans all the Availability Zones in the region
    - VPC Flow logs
    - users private cloud in a region
 - **Subnets**
    - logicl grouping of resources within the VPC
    - public subnet - can access from interent
    - private subnet
    - You can create one or more subnets within each availability zone but subnets **cannot** span across availability zones.
 - **Internet Gateway** connects VPC to internet
 - **VPC peering connection** is a networking connection between two VPCs that enables you to route traffic between them privately. Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.
 - Virutal Private Gateway
    - allows access to private resources in a VPC
 - AWS **Direct Connect**
    - dedicated private/physical connection between your data center and a VPC
    - Benefits of AWS Direct Connect
        – Reduce cost when using large volumes of traffic.
        – Increase reliability (predictable performance).
        – Increase bandwidth (predictable bandwidth).
        – Decrease latency.
- **Elastic IP**
    - addresses are for use in a specific region only and can therefore only be remapped between instances within that region.
    - You can use Elastic IP addresses to mask the failure of an instance in one Availability Zone by rapidly remapping the address to an instance in another Availability Zone.

### Subnets and network acces control list (ACL)

- **Subnets**
    - section of a VPC ; group resources based on a security or operational needs
    - public and private subnets
    - each subnet is assoicated with a **route table**, which specifies the routes for outbound traffic leaving the subnet
- **Network Acces Control List (NACL)** 
    - VPC component that checks packet permissions
    -  firewall at the subnet level within a VPC
    - optional layter of security for VPC; usually left with default values; act as firewall for controlling traiffc in/out of subnets
    - stateless packet filtering; allows all inbound/outboutnd traffic
- a **Network Address Translation (NAT) gateway** allows resources in a private subnet to connect to internet
- Guide: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- **Security Groups** 
    - firewall that is associated with an EC2 instances
    - virtual firewall that controls inbound/outboutnd traffic for EC2 instance
    - Secures EC2 instances in the subnet
    - stateful packet filtering; denies all inbound/outboutnd traffic by default 
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html
- VPC Peering
-   connect 2 VPCs privately using AWS network
-   not transitive 
- VPC Endpoints
-   allows you to connect to AWS services using private network 
- VPC Endpoit gateway: give VPC access to S3, DynamoDB
- Site to Site VPN & Direct Connect
- IPV4 CIDR 10.0.25.0/24 means the subnet contains ip addresses from 10.0.25.0 to 10.0.25.255

### Global networking

- DNS (Route 53)
    - uses route 53 routing policies
    
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
   - primary benefits: High availability AND Elasticity
   - https://aws.amazon.com/elasticloadbalancing 

### Messaging and queuing

- aim for loosely coupled architecture
- Amazon Simple Notification Service (Amazon **SNS**)
    - publish/subscribe service. 
- Amazon Simple Queue Service (Amazon **SQS**)
    - message queuing service
    - asynchorouse integration between app components
    
### Serverless computing

- “serverless” means that your code runs on servers, but you do not need to provision or manage these servers. 
- AWS Lambda is a service that lets you run code without needing to provision or manage servers. 

#### AWS Lambda

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.
https://aws.amazon.com/lambda/

- serverless event-driven code execution; 
- trigger invokes lamda function 
- runs your application code only when needed without needing to run servers
- 15 min run time
- scales automatically
- monitor/log using CloudWatch        

## Containers

### AWS ECS

- fully managed container orchestration service

[https://aws.amazon.com/ecs/](https://aws.amazon.com/ecs/)

### Amazon Elastic Container Service (ECS)
- https://aws.amazon.com/ecs/
- fully managed container orchestration service

### AWS EKS

Amazon Elastic Kubernetes Service (Amazon EKS) gives you the flexibility to start, run, and scale Kubernetes applications in the AWS cloud or on-premises.

[https://aws.amazon.com/eks/](https://aws.amazon.com/eks/)

### AWS Fargate

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). 

[https://aws.amazon.com/fargate/?nc=sn&loc=1](https://aws.amazon.com/fargate/?nc=sn&loc=1)

#### AWS ECR

Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy your container images and artifacts anywhere

[https://aws.amazon.com/ecr/](https://aws.amazon.com/ecr/)

- amazon version of Docker Hub

##  Storage

### Instance store 

- provides temporary block-level storage for an Amazon EC2 instance
- lost when EC2 instance is terminated

### EBS - Elastic Block Store
- block-level storage volumes that you can use with Amazon EC2 instances
- allows incremental snapshot backups
- EBS volumes store data within a single Availability Zone
- need to be same AZ to attach EC2 instances
- Both non-root and root volumes can be encrypted
-  It uses AWS Key Management Service (AWS KMS) customer master keys (CMK) when creating encrypted volumes and snapshots.
- https://aws.amazon.com/ebs
- Making an Amazon EBS volume available for use on Linux - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
- EBS Charges
    - Provisioned IOPS
    - The amount of data storage provisioned(not consumed) per month

### AWS S3 - Simple Storage Service
 - object-based storage system that stores objects that are comprised of **key, value pairs**
 - object level storage and distribtuon for the internet
    - In object storage, each object consists of data, metadata, and a key.
 - max size is 5 TB
 - part of Amazon CloudFront
 - 99.999999 % durability
 - security
    - IAM Policy, S3 encyrption, bucket policy
 - static web site hosting
 - storage classes
    - S3 Standard
        - Stores data in a minimum of three Availability Zones
    - S3 Standard-Infrequent Access (S3 Standard-IA)
        - access less frequently but rapid access
    - S3 One Zone-Infrequent Access (S3 One Zone-IA)
        - Stores data in a single Availability Zone and lower cost
    - S3 Intelligent-Tiering
        - Ideal for data with unknown or changing access patterns
- S3 Transfer Acceleration
    - enables fast, easy, and secure transfers of files over long distances between a client and an Amazon S3 bucket
- **Replication** enables automatic, asynchronous copying of objects across Amazon S3 buckets.
    - Both source and destination buckets must have versioning enabled
    - Buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can copy objects between different AWS Regions or within the same Region.     
### S3 Glacier
- archving service
- data access
    - expedited: 1-5 mins
    - standard 3-5 hours
    - bulk; 5-12 hours

    - https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-two-steps.html
- S3 Glacier
    - Low-cost storage designed for data archiving
    - Able to retrieve objects within a few minutes to hours
- S3 Glacier Deep Archive
    - Lowest-cost object storage class ideal for archiving
    - Able to retrieve objects within 12 hours
- Allows [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html)
- S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions
- must have versioning enabled
- Bucket policies are used for controlling access to buckets
- Lifecycle management 
- create rules to automatically transfer objects between different storage classes
- https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html

### Storage fees
- With the standard storage class you pay a **per GB/month storage fee**, and **data transfer out** (data egress) of S3
- Standard-IA and One Zone-IA have a minimum capacity charge per object. 
- Standard-IA, One Zone-IA, and Glacier also have a retrieval fee. You don’t pay for data into S3 under any storage class.


## AWS Storage Gateway
- **hybrid cloud storage** service that gives you **on-premises** access to virtually unlimited cloud storage
- three different types of gateways 
    - File Gateway
        - Store and access objects in Amazon S3 from NFS or SMB file-based applications with local caching
    - Tape Gateway
        - Backup and archive on-premises data to virtual tapes in AWS
        -  supports all leading backup software
    - Volume Gateway 
        - Hybrid cloud block storage with local caching
        
### EFS - Elastic File System
- file storage
- EFS file systems store data across multiple Availability Zones.
- mutliple resources can access the same data at the same time
- only linux based AMI
- automatically scales

## Databases

- **Amazon RDS - RelationAL Database Service**
    - https://aws.amazon.com/rds/
    - managed DB by AWS
        - Postgress, MySQL, mariadb, oracle, ms sql, Aurora (aws db)
    - Automatic backup
    - DB snapshots - triggerd by user
    - Can only scale vertically; use read replicas for horizonal scaling
    - Charged for Multi AZ and outbound dta transfer
    - RDS **Read replicas** for read scalability
        - up to 5; ASYNC replication
        - [https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)
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
    - enable fault tolerance by using [Mutliple AZs](https://aws.amazon.com/rds/features/multi-az/)
    - Point-in-time recovery
        - You can restore an Amazon RDS database instance to a specific point in time with a granularity of 5 minutes
    - Enable automatic patching for the instances using the Amazon RDS console
    - **Amazon Aurora**
        - fully managed; proprietary DB technology from AWS
        - mysql and psql
        - Automatically grows; 10GB increments
        - up to 15 replicas
        - aurora serverless - only runs when u need it
- **DynamoDB**
    - serverless db
    - offers flexible schema and can easily handle **unstructured data**.
    - nonrelational; nosql key/value db
    - highly scalable
- **AWS Redshift**    
    - data warehousing service that you can use for big data analytics
    - columnar db, petabyte warehouse; 1000 TB = 1 PB
    - can be reserved
- Additional database services
    - **Amazon DynamoDB Accelerator (DAX)** is an in-memory cache for DynamoDB. 
    - **Netptune**
        - managed Graph db
    - **AWS ElaticCache**
        - in memory databases; Redis or MemCached
        - RDS for caches; relieves load on RDS
        - can store user sessions
### AWS Database Migration Service (AWS DMS)

- enables you to migrate relational databases, nonrelational databases, and other types of data stores.
- move data between a source database and a target database
-  The source and target databases can be of the same type or different types

## Analytics

### Amazon Elastic MapReduce (Amazon EMR) 

- big data
- managed **Hadoop framework** that makes it easy, fast, and cost-effective to process vast amounts of data across dynamically scalable Amazon EC2 instances
- process vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto.
  
### AWS Athena

- serverless service to peroform anlayltic directly against S3 files
- uses SQL
- https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/


## DynamoDB 

- NoSQL serverless DB
- fully managed by AWS w/ replication across 3 AZ
- Made of tables; 
- Amazon DynamoDB Accelerator (DAX) 
    - provides in-memory acceleration to tables that result in significant performance improvements

https://aws.amazon.com/dynamodb/

## Reservations
   - Amazon ElastiCache and Amazon Redshift 

## Amazon Elasticsearch 
- Service is involved with operational analytics such as application monitoring, log analytics and clickstream analytics. 
   

## Ways To Interact with/Provision AWS Services

### AWS Management Console
 - use MFA - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html

### AWS CLI

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

### AWS SDK
- perfomr actions on AWS directly from your app w/o using CLI
-https://aws.amazon.com/tools/
- AWS CLI uses Python SDK (boto3)

    
## Security & Compliance

- https://aws.amazon.com/compliance/
- https://aws.amazon.com/compliance/programs/
- https://aws.amazon.com/artifact/


## AWS Step Functions 
 - lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly.
 - asynchorouse integration between app componets 

##AWS Developer Tools

### AWS Cloud9

- free shared IDE using browser; real time; direct terminal access
- option to run: ec2 + aws cloud9 OR your server + aws cloud9
- for versioing use AWS codecommit or other remote rep (GitHub, etc)
- [https://aws.amazon.com/cloud9/](https://aws.amazon.com/cloud9/)

### AWS CodeStar

[https://aws.amazon.com/codestar/](https://aws.amazon.com/codestar/)
### AWS CodeCommit

fully-managed source control service that hosts secure Git-based repositories.

- free; backed by S3
- [https://aws.amazon.com/codecommit/](https://aws.amazon.com/codecommit/)
- [Setup](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html)

### AWS CodeBuild

fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. 

[https://aws.amazon.com/codebuild/](https://aws.amazon.com/codebuild/)

- No build servers to manage
- Monitor build throught CloudWatch events
- alternative to Jenkins, Bamboo, TeamCity, [AWS QuickStart](https://aws.amazon.com/quickstart)
- [Build Spec YAML File](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)

### AWS CodeDeploy 

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

### AWS CodePipeline

- fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. 
- CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define. This enables you to rapidly and reliably deliver features and updates. You can easily integrate AWS CodePipeline with third-party services such as GitHub or with your own custom plugin. With AWS CodePipeline, you pay for only what you use. There are no upfront fees or long-term commitments.
- [Docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
- [Actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions.html)
    - parallel/sequential/manual approvals

# Security, Identity, & Compliance


### Shared Responsibility Model 

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates.

- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- AWS is responsible for:
    - Security "of" the Cloud 
    - For a service like Amazon EC2, that falls under Infrastructure as a Service, AWS is responsible for maintaining guest operating system 
    - AWS is responsible for training AWS and customer employees on AWS products and services
- Customer is responsible for:
    - security "in" the cloud
    - patching software on EC2 instances
    - set S3 object permissions
    - Configuration Management is the responsibility of the customer 

### User Permissions and Access

#### IAM (Identity and Access Management )

- whole AWS security is here; users, groups, role
- IAM is global; across regions
- permissions are govered by poliies (JSON)
- multi-factor authentication (MFA) 
- MFA options
    - Virtual MFA devices.
    - U2F security key
    - Hardware MFA device
    - SMS text message-based MFA
- Supported authentication methods include console passwords, access keys and server certificates.
- IAM User
    - One IAM User per physical person
- IAM Policy
    - JSON Doc that allows or denies permissions
- IAM groups
    - collection of IAM users
    - attch policy to group
- IAM Role
    - assoicated permissions; allow or deny
    - entity used for assigning permissions to AWS services
    - access to temporary permissions
    - one IAM role per application
    - IAM roles are ideal for situations in which access to services or resources needs to be granted temporarily, instead of long-term.  
- IAM Federation; for big enterprises
    - uses SAML Standard (AD)
- use IAM **access advisor** to identify unnecessary permisons that hab been assigned to users
- Best practices:
    - root user acct should never be used/shared
    - never use ROOT accont except for initial setup; 
    - create a new IAM user and assign permissions to create other users
    - Follow the security principle of **least privilege** when granting permissions. 
- by default new user has access to nothing
- Users can be assigned an **access key ID** and **secret access key** for programmatic access to the AWS API, CLI, SDK, and other development tools and a password for access to the management console.
- Access keys are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).
    - Best practices include
        - Don’t generate an access key for the root account user.
        - Use Temporary Security Credentials (IAM Roles) Instead of Long-Term Access Keys.
        - Manage IAM User Access Keys Properly.
- Server certificates are **SSL/TLS certificates** that you can use to authenticate with some AWS services.

### Amazon Cognito
-  lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily
####  AWS Web Application Firewall (WAF) 
- protect web applications or APIs against common web exploits. Rules can be created that block traffic based on source IP address.
 
#### Amazon Macie

 Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS. Macie automatically provides an inventory of Amazon S3 buckets including a list of unencrypted buckets, publicly accessible buckets, and buckets shared with AWS accounts outside those you have defined in AWS Organizations. Then, Macie applies machine learning and pattern matching techniques to the buckets you select to identify and alert you to sensitive data, such as personally identifiable information (PII).

#### AWS Secrets Manager
AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets with a call to Secrets Manager APIs, eliminating the need to hardcode sensitive information in plain text. It cannot be used to discover and protect your sensitive data in AWS.


#### AWS Acceptable Use Policy

The Acceptable Use Policy describes prohibited uses of the web services offered by Amazon Web Services, Inc. and its affiliates (the “Services”) and the website located at http://aws.amazon.com (the “AWS Site”). This policy is present at https://aws.amazon.com/aup/ and is updated on a need basis by AWS.

https://aws.amazon.com/aup/

### AWS Organizations

use [AWS Organizations](https://aws.amazon.com/organizations) to consolidate and manage multiple AWS accounts within a central location.

- centralized management
- [Consoldate billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) for all member accounts
- bulk discount
- grouping of accounts; organizational units (OU)
- AWS service and API actions access control
    - SCPs(Service control policy)
        - enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access.
        - you can apply service control policies (SCPs) to the organization root, an individual member account, or an OU
- Automate the creation of AWS accounts and categorize workloads using groups
- When using AWS Organizations with consolidated billing, best practices include:
    - Always enable multi-factor authentication (MFA) on the root account.
    - Always use a strong and complex password on the root account.
    - The Paying account should be used for billing purposes only. Do not deploy resources into the Paying account.
- Best practices:
    - Create accounts per department
    - restrict account privileges using Service Control Policies (SCP)
There is a default limit of 20 linked accounts but this can be extended and there is no reason why you should stick to a maximum of 20 accounts.

### Denial-of-service attacks
- deliberate attempt to make a website or application unavailable to users.
- use security groups and tools below to prevent:
    - **AWS Shield**
         - service that protects applications against DDoS attacks. 
         - AWS Shield provides two levels of protection: 
            - Standard (free)
            - Advanced (paid)
                -  provides enhanced detection and includes a specialized support team for customers on Enterprise or Business support plans. 
    - **AWS WAF (Web Application Firewall)**
        - web application firewall that lets you monitor network requests that come into your **web applications**.
        - security rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns you define. 

### Compliance

#### AWS Artifact 
- compliance information resource
- service that provides on-demand access to AWS security and compliance reports and select online agreements.
- AWS Artifact Agreements
- AWS Artifact Reports
-  Customer Compliance Center contains resources to help you learn more about AWS compliance. 

   
### AWS Config 
- fully-managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and regulatory compliance.
-  organization track resource inventory and configuration history for the purpose of security and regulatory compliance

### Encryption

-  encryption is automatically enabled for following AWS services:
    - Amazon S3 Glacier
    - AWS Storage Gateway

### Additional Security Services

#### AWS Key Management Service (AWS KMS)
 - enables you to perform encryption operations through the use of cryptographic keys.
 - ensure that your applications’ data is secure while in storage (encryption at rest) and while it is transmitted, known as encryption in transit.
 - [KMS](https://aws.amazon.com/kms/)


#### AWS Inspector 
- **automated security assessment service** that helps improve the security and compliance of applications deployed on AWS
-  checks applications for security vulnerabilities and deviations from security best practices, such as open access to Amazon EC2 instances and installations of vulnerable software versions.

#### Amazon Guard​Duty
- **threat detection service** that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data stored in Amazon S3. 
- provides intelligent threat detection for your AWS infrastructure and resources.


##  Monitoring and Analytics

### [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

-  performs **app performance** monitoring and can monitor custom metrics generated by applications and the **operational health** of your AWS resources
- create alarms that automatically perform actions if the value of your metric has gone above or below a predefined threshold. 
- **CloudWatch dashboard** feature enables you to access all the metrics for your resources from a single location. 
- monitors applications  in real time. 
- allows billing alarms
- provides data and actionable insights to monitor applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health.

### CloudTrail

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. 
https://aws.amazon.com/cloudtrail/

- Track user activities and **API requests/calls** throughout your AWS infrastructure
- log, monitor and retain account activity related to actions across your AWS infrastructure
- used for logging who does what in AWS by recording API calls. It is used for auditing, not performance or system operational monitoring.
- Automatically detecting unusual account activity
- Filter logs to assist with operational analysis and troubleshooting
-  CloudTrail Insights
    - OPTIONAL FEATURE allows CloudTrail to automatically detect unusual API activities in your AWS account. 


### AWS Trusted Advisor

- [Trusted] Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) is an online resource that helps to reduce cost, increase performance and improve security by optimizing your AWS environment.
-  inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices. The inspection includes security checks, such as Amazon S3 buckets with open access permissions.
- Trusted Advisor provides real time guidance to help you provision your resources following best practices.
- Advisor will advise you on Cost Optimization, Performance, Security, and Fault Tolerance.
- scans your AWS infrastructure and compares is to AWS best practices in five categories:
    - Cost Optimization
    - Performance
    - Security
    - Fault Tolerance
    - Service Limits


### X-Ray

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. 

https://aws.amazon.com/xray/


## Serverless

Serverless is the native architecture of the cloud that enables you to shift more of your operational responsibilities to AWS, increasing your agility and innovation. Serverless allows you to build and run applications and services without thinking about servers. It eliminates infrastructure management tasks such as server or cluster provisioning, patching, operating system maintenance, and capacity provisioning.

https://aws.amazon.com/serverless/
- exmples
    - AWS Lambda and Amazon API Gateway are both app-facing components of the AWS Serverless infrastructure


## Migration
- AWS Migration Hub
- AWS Database Migration Service
- AWS Server Migration Service

## Pricing and Support

### Free Tier

Three types of offers are available: 
- Always Free
    - auto scaling
    - IAM
- 12 Months Free
- Trials

### AWS pricing concepts
- Pay for what you use.
- Pay less when you reserve.
- Pay less with volume-based discounts when you use more.
- **AWS Pricing Calculator** lets you explore AWS services and create an estimate for the cost of your use cases on AWS.
- **AWS Billing & Cost Management dashboard** to pay your AWS bill, monitor your usage, and analyze and control your costs. 
- Consolidated billing for AWS Organizations
    - single bill for all AWS accounts in your organization. 
    -  ability to share bulk discount pricing, Savings Plans, and Reserved Instances across the accounts in your organization.
    - The default maximum number of accounts allowed for an organization is 4
- APN Consulting Partners
     - help an organization to design, build, and manage their workloads on AWS
### AWS Cost Management
- **AWS Cost Explorer** is a tool that enables you to visualize, understand, and manage your AWS costs and usage over time.
    - cost reports
    -  forecast your AWS account usage and costs
- **AWS Budgets**, you can create budgets to plan your service usage, service costs, and instance reservations.
- **AWS Marketplace** is a digital catalog that includes thousands of software listings from independent software vendors. You can use AWS Marketplace to find, test, and buy software that runs on AWS. 
    - one-click deployment
    - 3-rd party software that runs on AWS
    - Sell Software as a Service (SaaS) solutions to AWS customers
    - AWS customer can buy software that has been bundled into customized AMIs by the AWS Marketplace sellers
###  Support Plans
- All support plans provide 24×7 access to customer service, documentation, whitepapers, and support forums.
- four different [Support Plans](https://aws.amazon.com/premiumsupport/plans/) to help you troubleshoot issues, lower costs, and efficiently use AWS services. 
    - **Basic** – billing and account support only (access to forums only).
        - FREE
        -  you can use the **AWS Personal Health Dashboard**, a tool that provides alerts and remediation guidance when AWS is experiencing events that may affect you.
            - [Service Health Dashboard](https://status.aws.amazon.com/)
                - shows service status
                - Allows rss fields
    - **Developer** 
        – business hours support via email.
        
        - open unlimited cases
    - **Business** – 24×7 email, chat and phone support.
        - open unlimited cases
        - All AWS Trusted Advisor checks
        - open production system down support case
    - **Enterprise** – 24×7 email, chat and phone support.
        - open unlimited cases
        - Designated **Technical Account Manager (TAM)** to proactively monitor your environment and assist with optimization and coordinate access to programs and AWS experts
            - provides expert monitoring and optimization
        - AWS Concierge
            - support AWS customers on an Enterprise support plan with account issues
        - open business-critical system down support
        -  provides access to online training with self-paced labs

- You use **Trusted Advisor** to visually confirm whether your account resource configurations
    - alerts are divided into five categories: Cost Optimization, Performance,
    - help you analyze your infrastructure to identify unattached or underutilized EBS volumes
Security, Fault Tolerance, and Services Limits
are sound and are compliant with best practices

 
 ## Automation Tools
 
- AWS Elastic beanstalk - deoploy code to cluod
- opswork - mange infrastructure
- cloudformation - define infrastructure

### AWS Elastic Beanstalk
- easy-to-use service for deploying and scaling web applications and services
- You can upload code directly using a **ZIP or WAR file**. You can also use a Git archive.
- uses Cloud Formation in backend
- platform as a service; managed service; developer responsible for code only
- beansstalk itself is free; pay for resources that make up app
- Beanstalk lifecycle policy
    - beanstak can store 1000 application versions
- Elastic Beanstalk - Single  Docker; not ECS uses EC2
- https://aws.amazon.com/elasticbeanstalk/
- deployment options: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html
- [Tutorials](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html)


### AWS Systems Manager
- gives you visibility and control of your infrastructure on AWS. 
- Systems Manager Command documents let you automate tasks against your instance operating
systems, such as patching, installing software, enforcing configuration settings, and
collecting inventory
- get operational insights of its resources to quickly identify any issues that might impact applications using those resources.
- provides a unified user interface so you can view operational data from multiple AWS services and **allows you to automate operational tasks** across your AWS resources.

### AWS OpsWorks
- configuration management service that provides managed instances of Chef and Puppet.

### AWS CloudFormation

- infrastruce as code
- declarative way of outling your AWS infrastructure using YAML/JSON; YAML is better for CF
-  AWS CloudFormation template formats - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html
- [stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
- AWS TaskCat
    - tests cloudformation templates

## AWS Glue
- serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
-  prepare and load data for analytics using an extract, transform and load (ETL) process

## Amazon Neptune
- a fast, reliable, fully-managed **graph database** service that makes it easy to build and run applications that work with highly connected datasets. 

## Migration, Transfer and Innovation

-  **[AWS Cloud Adoption Framework (AWS CAF)](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf)** organizes guidance into six areas of focus, called Perspectives:
    - People Perspective
    - Governance Perspective
    - Platform Perspective
    - Security Perspective
    - Operations Perspective

- 6 strategies for migration (6 Rs)
    - Rehosting
    - Replatforming
    - Refactoring/re-architecting
    - Repurchasing
    - Retaining
    - Retiring
    
### AWS Snow Family members
-  composed of AWS Snowcone, AWS Snowball, and AWS Snowmobile. 
    - **AWS Snowcone** 
        - small, rugged, and secure edge computing and data transfer device. 
    - **AWS Snowball**
        - suitcase-sized data migration and edge computing device that comes in two device options: 
          - Compute Optimized and Storage Optimized. 
        - Snowball Edge Storage Optimized devices provide 40 vCPUs of compute capacity coupled with 80 terabytes of usable block or Amazon S3-compatible object storage. 
        -  move up to 80TB per device. AWS call this a “petabyte-scale data transfer service”.
    - **AWS Snowmobile**
        - move 100PB per snowmobile. AWS call this an “**Exabyte**-scale data transfer service”.
        - **shipping container**  moved with a tractor-trailer. These services can assist with data migration, disaster recovery, data center shutdown, and remote data collection projects.

### Amazon Elastic Transcoder 
 - is a highly scalable, easy to use and cost-effective way for developers and businesses to convert (or “transcode”) video and audio files from their source format into versions that will playback on devices like smartphones, tablets and PCs.
### Amazon Rekognition 
- Automate your image and video analysis with machine learning.

You can create one or more subnets within each availability zone but subnets cannot span across availability zones.

## Internet of Things

### AWS IoT Core 
 - managed cloud service that lets connected devices easily and securely interact with cloud applications and other devices.

##  Amazon WorkSpaces 
  - a managed, secure cloud desktop service 
  
## Amazon SageMaker 
- fully-managed platform that enables developers and data scientists to quickly and easily build, train, and deploy **machine learning** models at any scale

## AWS Quick Starts 
- help you deploy popular technologies on AWS, based on AWS best practices for security and high availability
- rapidly deploy a popular IT solution and start using it immediately.

## [Amazon Transcribe](https://aws.amazon.com/transcribe/) 
- used for language translation
- Amazon Translate uses neural machine translation via deep learning models to deliver more accurate and more natural-sounding translation than traditional statistical and rule-based translation algorithms.
- convert speech to text for downstream analysis

## [Amazon Polly](https://aws.amazon.com/polly/) 
- to convey the text results via speech

## [AWS Single Sign-On (SSO)](https://aws.amazon.com/single-sign-on/)
- enables you to makes it easy to centrally manage access to multiple AWS accounts and business applications and provide users with single sign-on access to all their assigned accounts and applications from one place.

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
- [Cloud Practioner](https://aws.amazon.com/certification/certified-cloud-practitioner/)
- [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf)
- [examp prep cheat sheets](https://digitalcloud.training/certification-training/aws-certified-cloud-practitioner)
- [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

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