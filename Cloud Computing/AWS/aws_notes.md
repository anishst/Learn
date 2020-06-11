# Amazon Web Services


- EC2 - Virtual machines
- VPC - Virtual Private Cloud
- AMI - Amazon Machine Image
    - EC2 is based off AMI
- ELB - Elastic Load Balancing

Service Summary - https://i.imgur.com/k013j1R.png

![Image](https://i.imgur.com/k013j1R.png)



## Amazon DB Services: DB options
- self-managed
    - db server on EC2; Bring ur own license
- fully managed
    - amazon RDS / amazon aurora
    - Amazon dynamodb
    - amazon redshift
## Setup

- regions
    - availablity zones; related to data centers
        - isolated from other zones
        - connecte by a low-latency link
        - edge locations host a CDN

## Auto Scaling

## Storage Services

EBS - Elastic Block Storage

### Simple Storage Service(S3)
 
 - object storage and distribtuon for the internet
 - part of Amazon CloudFront
 - 99.999999 % durability
 - can be used to shift static content from web instances
 - storage classes
    - standard
    - standard - infrequent access
    - glacier

### Automation Tools
- AWS Elastic beanstalk - deoploy code to cluod
- opswork - mange infrastructure
- cloudformation - define infrastructure

## Database

- Dynamo

## Compliance

- https://aws.amazon.com/compliance/
- https://aws.amazon.com/compliance/programs/
- https://aws.amazon.com/artifact/

## Encryption

https://aws.amazon.com/kms/

## Security

- white paper: https://d1.awsstatic.com/whitepapers/aws-security-whitepaper.pdf
- Security, Identity, and Compliance: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-services.html
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

https://aws.amazon.com/certification/

## Training
- awesome day: https://aws.amazon.com/events/awsome-day/
- workshops: https://aws.amazon.com/serverless-workshops/