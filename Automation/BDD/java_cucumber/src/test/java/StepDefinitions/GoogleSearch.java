package StepDefinitions;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class GoogleSearch {


	WebDriver driver = null;


	@Given("User is on Google Search Page")
	public void user_is_on_google_search_page() {
		System.out.println("User is on search page");

		//	get current directory - only needed if webdriver is not in Path
		//	String projectPath = System.getProperty("user.dir");
		//	System.out.println("Project path is: " + projectPath);
		//	System.setProperty("webdriver.chrome.driver", projectPath+"/src/test/resources/drivers/chromedriver.exe");

		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(30,TimeUnit.SECONDS);
		driver.manage().timeouts().pageLoadTimeout(30,  TimeUnit.SECONDS);
		driver.navigate().to("http://www.google.com");
	}

	@When("I enter search term in box")
	public void i_enter_search_term_in_box() {
		driver.findElement(By.name("q")).sendKeys("Java");
		
	}

	@When("I click on Search button")
	public void i_click_on_search_button() {
		driver.findElement(By.name("q")).sendKeys(Keys.ENTER);
	}

	@Then("Show Results")
	public void show_results() throws InterruptedException {
		driver.findElement(By.linkText("Java")).isDisplayed();
		driver.findElement(By.linkText("Java")).click();
		Thread.sleep(3000);
		driver.quit();
	}





}
