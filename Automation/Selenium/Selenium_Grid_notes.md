# Selenium Grid

Selenium Grid is a part of the Selenium Suite that specializes in running multiple tests across different browsers, operating systems, and machines in parallel.

### When to use
- To run tests on multiple browsers and their versions, different devices, and operating systems
- To reduce the time that a test suite takes to complete a test

## Download

https://www.seleniumhq.org/download/
Selenium Standalone Server


Docs:
https://github.com/SeleniumHQ/selenium/wiki/Grid2

https://www.selenium.dev/documentation/en/grid/setting_up_your_own_grid/

## Selenium 3 Grid

1. download JAR - Selenium Server (Grid): https://www.selenium.dev/downloads/
2. Start the hub;```java -jar selenium-server-standalone-<version>.jar -role hub```
3. Check status by going to grid console:  http://localhost:4444/grid/console
4. start the nodes

- For local runs:
    - DEFAULT nodes (1 ie, 5 firefox, 5 chrome) - ```java -jar selenium-server-standalone-3.141.59.jar -role node  -hub http://localhost:4444/grid/register```
    - IE nodes only: ```java -Dwebdriver.ie.driver=C:/SeleniumSetup/webdriver/IEDriverServer.exe -jar selenium-server-standalone-3.141.59.jar -port 4567 -role node -hub http://localhost:4444/grid/register -browser "browserName=internet explorer,version=11,platform=WINDOWS,maxInstances=5"```
    - Chrome nodes only: ```java -Dwebdriver.ie.driver=C:/SeleniumSetup/webdriver/chromedriver.exe -jar selenium-server-standalone-3.141.59.jar -port 5567 -role node -hub http://localhost:4444/grid/register -browser "browserName=chrome,version=11,platform=WINDOWS,maxInstances=5"```

- Remote run: ```java -jar selenium-server-standalone-2.48.2.jar -role node```. If you are running node from another machine, that machine need the standalone JAR as well.
- Remote run from another machine: ```java -jar selenium-server-standalone-2.48.2.jar - role webdriver -hub http://10.253.164.119:4444/grid/register -port 5566```; the hub ip can found in the hub console window: example: Nodes should register to http://10.253.164.119:4444/grid/register/


python test example:
https://www.youtube.com/watch?v=nDZgYDqoPqc&t=66s

Run test using this from cmd windows:
```
py.test -n 3 Grid_test_with_unittest.py
```

## Selenium 4 Grid

1. download JAR: https://selenium-release.storage.googleapis.com/4.0/selenium-server-4.0.0-alpha-1.jar
NOTE: make sure webdriver files are in the same folder as the standalone jar
2. launch by: ```java -jar selenium-server-4.0.0-alpha-1.jar standalone``` 
3. check status by going to: http://localhost:4444/status

More info: https://github.com/SeleniumHQ/selenium/wiki/Selenium-Grid-4


## Guides

- https://testdriven.io/blog/distributed-testing-with-selenium-grid/

## Video Tutorials

- https://www.youtube.com/watch?v=phJoABOXmqM



## Docker Selenium Grid

https://github.com/SeleniumHQ/docker-selenium

### Using Chrome standalone image

1. downloand image: ```docker pull selenium/standalone-chrome``` or ```docker pull selenium/standalone-chrome:latest```
    - https://hub.docker.com/r/selenium/standalone-chrome/
2. run container: ```docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:latest```
    - -d tells to run in background
    - -p hostport/container port
    - more info on run commands: https://github.com/SeleniumHQ/docker-selenium#running-the-images
3. check status: ```docker ps```  
4. Use example script to run from Java

```java
public class chromeStandAlone {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub
		
		DesiredCapabilities cap = DesiredCapabilities.chrome();
	
		URL url = new URL("http://localhost:4444/wd/hub");
		RemoteWebDriver driver = new RemoteWebDriver(url, cap);
		driver.get("http://www.google.com");
		System.out.println(driver.getTitle());
		driver.quit();
	}
}
```

example 2
```java
package selenium_docker;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class chromeStandAlone {

	public static void main(String[] args) throws MalformedURLException {
		// To test with local docker launch  chrome image: docker run --privileged -d -p 4444:4444 selenium/standalone-chrome
		//	verify hub at: http://localhost:4444/wd/hub
		
		DesiredCapabilities cap = DesiredCapabilities.chrome();
		cap.setBrowserName("chrome");
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--no-sandbox");
		options.addArguments("--disable-dev-shm-usage");
		options.addArguments("--headless");
		options.addArguments("--disable-gpu");
		options.addArguments("--screen-size=1200x800");
		options.merge(cap);
		URL url = new URL("http://localhost:4444/wd/hub");
		RemoteWebDriver driver = new RemoteWebDriver(url, cap);
		driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.get("http://www.google.com");
		System.out.println(driver.getTitle());
		driver.get("http://www.python.org");
		System.out.println(driver.getTitle());
		driver.quit();

	}

}
```

### Steps for setup using Hub 
1. Install images:
   -  ```docker pull selenium/hub``` 
   -  ```docker pull selenium/node-chrome```
   - ```docker pull selenium/node-firefox```
2. Run images: 
    - 
    - ```docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-firefox:3.141.59-vanadium```

- ```HUB_HOST``` env variable is available for all nodes so they can see the HUB; HUB_HOST=hub

### Connecting to Debug mode images using VNC Viewer

1. download vnc viewer: https://www.realvnc.com/en/connect/download/viewer/
2. download/run chrome debug image: ```docker run -d -P -p 4444:4444 selenium/standalone-chrome-debug```
3. run ```docker ps``` to get vnc port; example: 0.0.0.0:**32768**->5900/tcp
4. launch vnc viewer and connect using:  localhost:32768
5. when you run your tests cases they will appear in the vnc viewer

### Guides

- https://www.browserstack.com/guide/selenium-grid-tutorial

### Videos
- https://www.youtube.com/watch?v=_lBaedX4UAE&t=385s
- https://bah.udemy.com/course/sdettraining-testarchitect-fullstackqa/learn/lecture/14445850#overview
- https://bah.udemy.com/course/selenium-webdriver-with-docker/learn/lecture/13299724?start=285#overview 
## Troubleshooing

Issue: 4444 port is being used 

1. Get process by id using powershell command: ```Get-Process -Id (Get-NetTCPConnection -LocalPort 4444).OwningProcess```
2. Kill by: ```Stop-Process *process_id*```

If above doesn't work try: 
- ```docker-compose down```
- ```docker rm -fv $(docker ps -aq)```

## Resources

- [Docker selenium tests code example](https://github.com/vinsguru/docker-selenium-test)
- [Selenium Docker](https://github.com/vinsguru/selenium-docker)