#!/usr/bin/env bash

echo "*************Running entry.sh file**********"
cd code/
pwd
ls

URL=${@}
echo "Starting JMeter tests on ${URL}"

#Command
cd ../bin
sh jmeter -n -t /opt/apache-jmeter-5.2.1/code/scripts/CSVSample.jmx -l /opt/apache-jmeter-5.2.1/code/test_output.csv -JThreadNumber=2 -JRampUpPeriod=1 -JURL=${URL} -f -e -o /opt/apache-jmeter-5.2.1/code/reports/

echo "********entry.sh file RAN SUCCESSFULLY*******"