# Splunk

Splunk indexes and correlates real-time data in a searchable repository from which it can generate graphs, reports, alerts, dashboards and visualizations

## Deployment Models
- Cloud or On-Premise
- [Guide PDF](https://www.splunk.com/themes/splunk_com/img/assets/pdfs/education/SplunkDeploymentGuide2_1.pdf)
- [Deployment options](https://docs.splunk.com/Documentation/PCI/4.5.0/Install/Deploymentoptions)

## Data Storage
- stored as indexes

## Licensing
- license data ingested per day, not data stored 
- [How Splunk Enterprise licensing works](https://docs.splunk.com/Documentation/Splunk/8.1.3/Admin/HowSplunklicensingworks)

## Forwarders
- universal
- heavy

## Searching in Splunk

- SPL (Search Processing Language)

## Linux folders

- /opt/splunk
- indexes: /var/lib/splunk/defaultdb
## Run with Docker

- [Docker image](https://hub.docker.com/r/splunk/splunk/)
- run: ```docker run -d -p 8000:8000 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=<password>" --name splunk splunk/splunk:latest```