package demoplot.DemoPlot;

import org.testng.annotations.Test;

import io.appium.java_client.AppiumBy;


public class AppiumBasics extends BaseTest {

     
	@Test
	public void KrishLogin() throws InterruptedException{
		Thread.sleep(70);
		driver.findElement(AppiumBy.id("com.carnot.krishefield:id/btn_submit")).click();
		
   }
}
