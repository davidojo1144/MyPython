public class DivideOrSquare{

	
		public double division(int number){
		number = 50;
		if (number % 5 == 0){
		double result = Math.sqrt(number);
		return result;
		}
		
		else {
		return number % 5 ;
		}

		}

		public static void main(String...args){
		DivideOrSquare divideorsquare = new DivideOrSquare();
		double result = divideorsquare.division(50);
		System.out.print("The result is: " + result);
		}


}

		

		
		