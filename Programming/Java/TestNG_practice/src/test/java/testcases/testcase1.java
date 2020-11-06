package testcases;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class testcase1  extends BaseTest {
	
	@BeforeTest
	public void createDB() {
		System.out.println("Db connection");
		
	}
	
	@AfterTest
	public void closeDB() {
		System.out.println("Closing Db");
		
	}
	
	
	@BeforeMethod
	public void launchBrowser() {
		
		System.out.println("Launching browser");
	}
	
	@Test(priority=1)
	public void doLogin() {
		
		System.out.println("Executing login test");
	}

	@Test(priority=2)
	public void doLogOut() {
		
		System.out.println("Logout test");
	}
	
	@AfterMethod
	public void closeBrowser() {
		System.out.println("Closing browser");
		
	}
}
