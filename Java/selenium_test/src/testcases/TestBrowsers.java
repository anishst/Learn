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
		
		//assumes Chrome driver env variable is set
		FirefoxDriver driver1 = new FirefoxDriver();
		driver1.get("http://www.google.com");
		driver1.quit();
	}

}
