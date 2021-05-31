package sender;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;

import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class BMS_Data_Sender_TestSuite {
	ILogger logger;
	int count;

	@Before
	public void setup() {
		logger = new ConsoleLogger();
	}

	@Test
	public void givenCount_lessThanOrEqualsZero_thenReturnNull() {
		count = 0;
		assertNull(new Stream_BMS_Data(logger).streamData(count));
	}
	
	 @Test 
	 public void  givenReadingLimit_whenGivenValue_thenReturnDataWithSizeOfGivenValue() 
	 {
		 count = 20;
		 List<BatteryParams> outputSize = new Stream_BMS_Data(logger).streamData(count); 
		 assertEquals(20,outputSize.size());
	  }
	 
	 @Test 
	 public void givenBattery_whenStreamingData_thenReturnData() 
	 { 
		 count = 30;
		 assertNotNull(new Stream_BMS_Data(logger).streamData(count));
	 }
}