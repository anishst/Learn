# Amazon Web Services (AWS)

- AWS was launched in 2006

Amazon Products: https://aws.amazon.com/products/

Service Summary - https://i.imgur.com/k013j1R.png

![Image](https://i.imgur.com/k013j1R.png)

AWS Foundtions services
https://image.slidesharecdn.com/hsbcandawsday-awsfoundations-170709164032/95/hsbc-and-aws-day-aws-foundations-7-638.jpg?cb=1499618785

AWS Platform Services

https://image.slidesharecdn.com/getting-started-on-aws-awsome-19b96808-0f60-4c92-96f1-d7937c855042-304968793-180413164036/95/getting-started-on-aws-awsome-day-2018-12-638.jpg?cb=1523637675

## Amazon DB Services: DB options
- self-managed
    - db server on EC2; Bring ur own license
- fully managed
    - amazon RDS / amazon aurora
    - Amazon dynamodb
    - amazon redshift
## Setup

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
## Amazon EC2

- Virtual machines that provides resizable compute capacity in cloud
- Amazon EC2 Instance Types: https://aws.amazon.com/ec2/instance-types/
- https://docs.aws.amazon.com/ec2/index.html
- instance lifecycle: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html
    - charged while in rebooting and running state
 - metadata: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
 - Purchase options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html
    - on-demand - pay as you go
    - reserved - 1-3 yr contract
    - dedicated - dedicated hardware; nonshared
    - spot - bidding unused instances

### Coonection Options for EC2

SSH

- create new key pair
- save PEM file
- edit Edit inbound rules to allow SSH (SSH /TCP / 25 / Anywhere)
- form a terminal window go to directly with PEM file and enter this command: ```ssh -i <file.pem> <amazon_ec2_user@ipaddress```
- on linux you might need give permissionS if get error "bad permissions" : ```chmod 400 file.pem```
- on windows make your the owner of the pem file; disable inheritance and make sure you only have accessa nd have full control
- Help: https://bah.udemy.com/course/selenium-webdriver-with-docker/learn/lecture/14317256#overview
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

Via browser using EC2 Instance connect

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html

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
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
```
Note: make to sure edit security group to allow HTTP access: Security Groups > web server security group > inbound rules tab > edit > add rule > type: HTTP Source: Anywhere > Save rules
### Getting log from EC2 instance

- Actions > Instance Settings > Get System Log

## Virtual Private Cloud (VPC)
 - for networking
 - users private cloud in a region
 - **Subnets**
    - logicl grouping of resources within the VPC
 - **Internet Gateway** connects VPC to internet
 - IPV4 CIDR 10.0.25.0/24 means the subnet contains ip addresses from 10.0.25.0 to 10.0.25.255
 - ech subnet is assoicated with a **route table**, which specifies the routes for outbound traffic leaving the subnet
 - a **network acces control list (ACL)** is an optional layter of security for VPC; usually left with default values; act as firewall for controlling traiffc in/out of subnets
 - a **Network Address Translation (NAT) gateway** allows resources in a private subnet to connect to internet
- Guide: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html


## AMI - Amazon Machine Image
 - EC2 is based off AMI; similiar to docker image
 - OS + setup of software pre-installed
 - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html

## ELB - Elastic Load Balancing

## AWS Management Console
 - use MFA 

## Direct Connect

## Storage Services

### EBS - Elastic Block Store
- for storing data on virtual drives
- https://aws.amazon.com/ebs

### Simple Storage Service(S3)
 
 - object storage and distribtuon for the internet
 - part of Amazon CloudFront
 - 99.999999 % durability
 - can be used to shift static content from web instances
 - storage classes
    - standard
    - standard - infrequent access
    - glacier
  - versioning: https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html

### Glacier

   - archving service

### Automation Tools
- AWS Elastic beanstalk - deoploy code to cluod
- opswork - mange infrastructure
- cloudformation - define infrastructure

#### Tools to record UI clicks:
- https://chrome.google.com/webstore/detail/console-recorder-for-aws/ganlhgooidfbijjidcpkeaohjnkeicba?hl=en
- console recorder: https://addons.mozilla.org/en-CA/firefox/addon/console-recorder/#:~:text=Extension%20Metadata&text=Click%20the%20orange%20Console%20Recorder,click%20the%20Start%20Recording%20button.


## Database
- Amazon RDS - Relations db service
    - https://aws.amazon.com/rds/
- DynamoDB - NoSQL DB
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

## Networking

## Resources
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