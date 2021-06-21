package sender;

public class BMS_Data_Sender {
	
	public static void main(String args[])
	{
		int count = 30;
		ILogger logger = new ConsoleLogger();
		new Stream_BMS_Data(logger).streamData(count);
	}
}
