package sender;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import com.google.gson.Gson;

public class Stream_BMS_Data 
{
	ILogger logger;
	List<BatteryParams> streamData = new ArrayList<>();

	Stream_BMS_Data(ILogger logger)
	{
		this.logger = logger;
	}
	
	public List<BatteryParams> streamData(int count) {
		if(count <= 0)
			return null;
		
		for (int i = 1; i <= count; i++) {
			streamData.add(new BatteryParams()
					.setTemperature(generateRandomValues(BatteryLimit.MIN_TEMPERATURE, BatteryLimit.MAX_TEMPERATURE))
					.setSoc(generateRandomValues(BatteryLimit.MIN_SOC, BatteryLimit.MAX_SOC))
					.setChargeRate(generateRandomValues(BatteryLimit.MIN_CHARGERATE, BatteryLimit.MAX_CHARGERATE)));
			
		}
		logger.printMessage(convertToJson());
		return streamData;
	}

	public float generateRandomValues(float minValue, float maxValue) {
		return (new Random().nextFloat() * (maxValue - minValue)) + minValue;
	}

	public String convertToJson() {
		Gson gson = new Gson();
		return gson.toJson(streamData);
	}

}
