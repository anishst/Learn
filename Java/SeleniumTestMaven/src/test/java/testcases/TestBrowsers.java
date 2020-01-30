package testcases;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class TestBrowsers {

	public static void main(String[] args) {

		// Usage examples: https://selenium.dev/selenium/docs/api/java/index.html

		// assumes Chrome driver env variable is set
		ChromeDriver driver = new ChromeDriver();
		driver.get("http://www.google.com");
		driver.quit();

	}

}
