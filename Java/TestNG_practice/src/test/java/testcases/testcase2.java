package testcases;

import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class testcase2 extends BaseTest {
	
//	using assertions
	@Test
	public void validate_titles() {
		String expected = "Hello";
		String actual = "Hello";
		
		Assert.assertEquals(actual, expected);
		
		//		create instance
		SoftAssert softAssert = new SoftAssert();
			
		softAssert.assertEquals(true, true);
		softAssert.assertEquals(true, false, "text box not found");
		//		verify all at the end to make test pass/fail
		softAssert.assertAll();
	}
}
