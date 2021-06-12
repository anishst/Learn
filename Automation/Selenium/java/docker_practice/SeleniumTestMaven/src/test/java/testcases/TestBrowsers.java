package testcases;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

import java.net.MalformedURLException;
import java.net.URL;

public class TestBrowsers {

	public static void main(String[] args) throws MalformedURLException {

		// Usage examples: https://selenium.dev/selenium/docs/api/java/index.html

		// assumes Chrome driver env variable is set
		// ChromeDriver driver = new ChromeDriver();

		// testing remote webdriver - us this to launch docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:latest
		WebDriver driver;
		String nodeURL;
		System.out.println("Connecting to Hub");
		nodeURL = "http://192.168.1.25:4444/wd/hub";
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--no-sandbox");
		options.addArguments("--headless");
		driver = new RemoteWebDriver(new URL(nodeURL), options);
		System.out.println("Hub connection is good!");


		driver.get("http://www.google.com");
		System.out.println(driver.getTitle());
		driver.get("http://www.python.org");
		System.out.println(driver.getTitle());
		driver.quit();

	}

}
