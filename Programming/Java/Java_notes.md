# Java

Java is a general-purpose programming language that is class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible.

## Simple Program: HelloWorld.java

```
public class HelloWorld {

	public static void main(String[] args) {
		System.out.println("Hello world!");
	}
}
```

To run: 
1. Compile: ```javac HelloWorld.java```
2. This will create a .class file
3. To see the output: ```java HelloWorld```

## Common files

- **EAR (Enterprise Application ARchive)** Java EE-based enterprise application; An EAR file requires a fully Java Platform, Enterprise Edition (Java EE)- or Jakarta Enterprise Edition (EE)-compliant application server, such as WebSphere or JBoss, to run
- **JAR (Java ARchive)** is Java Application Archive that runs a desktop application on a user's machine. contain libs and property file 
- **WAR (Web Application ARchive)** file is a Web Application Archive which runs inside an application server. A war file is a special jar file that is used to package a web application to make it easy to deploy it on an application server. contains files for servlet container. includes JSP, HTML, JS files 
- both are zip files created using java tool

## Temp method for setting Java complier path
```set path=C:\Program Files\Java\jdk-11.0.1\bin```

## Eclipse

### Sharing Code

- generate JAR file by right clicking on project > export > Java > JAR File and save
- then you can use it another project by adding JAR as external reference lib

### Shortcuts

CTRL + Shift + L - format code

## Java Selenium Setup

- create new project
- right click on project and add selenium jar (selenium-server-standalone-3.141.59.jar); Build Path > add external archives

Sample test:
```java
package testcases;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class TestBrowsers {

	public static void main(String[] args) {
		
		//Usage examples: https://selenium.dev/selenium/docs/api/java/index.html
		
		//assumes Chrome driver env variable is set
		ChromeDriver driver = new ChromeDriver();
		driver.get("http://www.google.com");
		driver.quit();
		
	}

}
```

## Test Frameworks

### Junit

### TestNG
TestNG is a testing framework inspired from JUnit and NUnit but introducing some new functionalities that make it more powerful 

- main site: https://testng.org/doc/
- can be setup using Maven dependeny or as a plugin (https://testng.org/doc/download.html) in Eclipse

simple test:
```
   @Test
    public void doLogin() {
	    System.out.println("Executing login test");
	}
```

- by default tests run using alphabetic order
- to control use priority;  ex. @Test(priority=1)
- annotations:
    - @Test - indicates test case
    - @BeforeMethod - run before each test case
    - @AfterMethod - run after each test case
    - @BeforeTest - runs before all test cases start
    - @AfterTest - runs after all test cases are done
    - @BeforeSuite - before entire class of tests
    - @AfterSuite - after entire class of tests
    
- assertions
    - Assert.assertEquals(actual, expected);
    - see full list: https://www.javadoc.io/doc/org.testng/testng/6.8.17/org/testng/Assert.html

- soft assertions
    - use when you want to continue after failures```SoftAssert softAssert = new SoftAssert();```

```
		//		create instance
		SoftAssert softAssert = new SoftAssert();
		
		softAssert.assertEquals(true, true);
		softAssert.assertEquals(true, false, "text box not found");
		//		verify all at the end to make test pass/fail
		softAssert.assertAll();
```

- test dependencies
    - can be used to skip a test case if dependant test case fails
    - see doc: https://testng.org/doc/documentation-main.html#dependent-methods

- create test suite
    - option 1: use xml file to create; https://testng.org/doc/documentation-main.html#testng-xml
    - option 2: in eclipse, right-click on project > TestNG >   Convert to TestNG; this will pick up all test cases with annotations
    
Sample xml file with 2 test suites:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="Suite">
  <test name="LoginTest">
    <classes>
      <class name="testcases.testcase1"/>
    </classes>
  </test> <!-- Test -->
     <test name="AllTests">
    <classes>
      <class name="testcases.testcase1"/>
      <class name="testcases.testcase2"/>
    </classes>
  </test> <!-- Test -->
  
</suite> <!-- Suite -->
```
- Test Groups
     - to group test cases; you can also include/exclude tests by updating the xml file
     - groups can be defined at the suite level and also at the test group level
     - more info : https://testng.org/doc/documentation-main.html#test-groups
 
- TestNG Listners
    - triggers that occur when certain even occurs
    - can be used to capture screenshots when fails
    - https://testng.org/doc/documentation-main.html#testng-listeners  
    
## Maven


Maven is a dependency management/build automation tool used primarily for Java projects. Maven addresses two aspects of building software: first, it describes how software is built, and second, it describes its dependencies. 

- https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html
- Getting started https://maven.apache.org/guides/getting-started/

### Maven setup 

#### Windows

- download binary zip archive. 	apache-maven-3.6.3-bin.zip : https://maven.apache.org/download.cgi
- configure gloabally on test machine by adding below env variables
    - new sys env: ```MVN_HOME``` / value: ```<path to mvv>```; ex. C:\Python\selenium\webdriver\apache-maven-3.6.3
    - add to path variable: %MVN_HOME%/C:\Python\selenium\webdriver\apache-maven-3.6.3\bin
    - check setup using cmd line: ```mvn --version```
    
- create new Maven project in Eclipse
    - new maven project
    - enter groupid : domainname.
    - enter artifact id: selenimtest
    - Finish
    - add Java selenium dependcies for selenium using pom.xml 
    (https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java/3.141.59)
  
    ```<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-api</artifactId>
    <version>3.141.59</version>
    </dependency>```

#### Linux

- Install: ```sudo apt-get install maven```
- [Guide](https://www.baeldung.com/install-maven-on-windows-linux-mac)
 
### Maven Commands
- ```mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false``` - setup a simple project once maven is setup 
- ```mvn package``` - build jar file in targe folder
- ```mvn clean``` - clean target folder
- ```mvn site``` - generates a site based upon information on the project's pom. You can look at the documentation generated under target/site.
- ```mvn test``` - runs test scripts

### Maven Troubleshooting


Issue: error when doing mvn test in Linux: ```[ERROR] Source option 5 is no longer supported. Use 6 or later.```

Fix: add this to pom.xml
```xml
<properties>
    <maven.compiler.source>1.6</maven.compiler.source>
    <maven.compiler.target>1.6</maven.compiler.target>
</properties>
```

### Maven with Docker

- [Official Docker Image](https://hub.docker.com/_/maven)
- [docker image examples](https://github.com/carlossg/docker-maven)

```dockerfile
# https://stackoverflow.com/questions/27767264/how-to-dockerize-maven-project-and-how-many-ways-to-accomplish-it
# Build stage
#
FROM maven:3.5-jdk-8 AS build  
COPY src /usr/src/app/src  
COPY pom.xml /usr/src/app  
RUN mvn -f /usr/src/app/pom.xml clean package
```

#### On Demand Run
run this from a maven project folder: ```docker run -it --rm --name my-maven-project -v "$(pwd)":/usr/src/mymaven -w /usr/src/mymaven maven:3.3-jdk-8 mvn clean install```

#### Docker file approach

### Spring Boot with Docker
- [Git Repo with examples](https://github.com/spring-guides/gs-spring-boot-docker)

#### POM

A Project Object Model or POM is the fundamental unit of work in Maven. It is an XML file (pom.xml) that contains information about the project and configuration details used by Maven to build the project. It contains default values for most projects.

- [example pom file](https://github.com/spring-guides/gs-spring-boot-docker/blob/master/complete/pom.xml)


## Resources
- Official Java Tutorial: https://docs.oracle.com/javase/tutorial/index.html
- JAR File usage: https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html
- Oracle Docs: https://docs.oracle.com/en/
