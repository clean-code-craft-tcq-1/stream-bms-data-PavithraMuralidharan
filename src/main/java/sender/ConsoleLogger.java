package sender;

public class ConsoleLogger implements ILogger {

	@Override
	public void printMessage(String senderData) {
		System.out.println(senderData);
	}

}
