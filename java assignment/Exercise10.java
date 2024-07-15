public class Excercise10{
	public static void main (String... args){
	
	double amountAtEndOfYear = 0;
	double year = 30;
	double annualRate = 7;
	double amountInvested = 1000;
	for (double number = 1; number <= 30; number++){
	amountAtEndOfYear = amountInvested * ((1 + (7/100)) *number);
	System.out.printf("%.2f%n", amountAtEndOfYear);
	}

	}

}