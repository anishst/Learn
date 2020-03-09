package testcases;

import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class testFailure extends BaseTest {
	
//	using assertions
	@Test
	public void fail_sc1() {
		Assert.fail("Failing test");
	
	}
}
