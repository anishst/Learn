echo off
echo ***********************************************************************
echo 			***  JENKINS Launcher ***
echo 			Author: Anish Sebastian
echo 			Last update: 5/13/2020
echo ***********************************************************************
echo Pulling Latest Selenium Python Framework code from GitHub...
REM cd <location to code folder>
REM cd C:\Jenkins\SeleniumPythonFramework
git pull
echo Latest code check complete!
echo Starting Jenkins...
cd C:\Jenkins
echo Setting JAVA HOME
SET JAVA_HOME=C:\Jenkins\JDK
echo Setting Jenkins Home directory...
SET JENKINS_HOME=C:\Jenkins\JENKINS_HOME
REM launch Jenkins; using port 9000 since 8080 is being used by offline application
java -jar jenkins.war --httpPort=9001