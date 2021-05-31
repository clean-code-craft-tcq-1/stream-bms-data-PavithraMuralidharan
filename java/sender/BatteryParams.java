package sender;

public class BatteryParams 
{
	private float temperature;
	private float soc;
	private float chargeRate;
	
	public float getTemperature() {
		return temperature;
	}
	
	public BatteryParams setTemperature(float temperature) {
		this.temperature = temperature;
		return this;
	}
	
	public float getSoc() {
		return soc;
	}
	
	public BatteryParams setSoc(float soc) {
		this.soc = soc;
		return this;
	}
	
	public float getChargeRate() {
		return chargeRate;
	}
	
	public BatteryParams setChargeRate(float chargeRate) {
		this.chargeRate = chargeRate;
		return this;
	}
}
