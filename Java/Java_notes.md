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
- 

## Maven


Maven is a build automation tool used primarily for Java projects. Maven addresses two aspects of building software: first, it describes how software is built, and second, it describes its dependencies. 

https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

### POM

A Project Object Model or POM is the fundamental unit of work in Maven. It is an XML file (pom.xml) that contains information about the project and configuration details used by Maven to build the project. It contains default values for most projects.

## Resources
- Official Java Tutorial: https://docs.oracle.com/javase/tutorial/index.html
- JAR File usage: https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html
- Oracle Docs: https://docs.oracle.com/en/
