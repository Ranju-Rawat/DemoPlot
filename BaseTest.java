package demoplot.DemoPlot;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;
import io.appium.java_client.service.local.AppiumServiceBuilder;

public class BaseTest {

	 AppiumServiceBuilder service;
	 AndroidDriver driver;
	 
	 @BeforeClass
	public void configAppium() throws MalformedURLException{
		try {
		 service = new AppiumServiceBuilder().withAppiumJS(new File("C:\\Users\\rawat\\AppData\\Roaming\\npm\\node_modules\\appium\\build\\lib\\main.js")).withIPAddress("127.0.0.1")
				 .usingPort(4723);
		//service.start();
		
		UiAutomator2Options options = new UiAutomator2Options();
		options.setDeviceName("Samsung Galaxy S4");
		options.setApp("C:\\Users\\rawat\\eclipse-workspace\\DemoPlot\\src\\app.apk");
		options.autoGrantPermissions();
        //driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        System.out.println("Service Print"+", "+service);
		 driver = new AndroidDriver(new URL("http://127.0.0.1:4723"), options);
	} catch (Exception e) {
        e.printStackTrace();
	} 
}
	
  @AfterClass
	public void Teardown() throws InterruptedException {
	 Thread.sleep(100);
		driver.quit();
	}
}



