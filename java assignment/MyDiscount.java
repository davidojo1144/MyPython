public class MyDiscount{

	
	public double division(int price, int discount){
	price = 500;
	discount = 20;
	double amountDiscounted = discount / 100;
	double result = price * 0.2;
	double finalPrice = price - result;
	return finalPrice;
	}

	public static void main(String...args){
	MyDiscount mydiscount = new MyDiscount();
	double finalPrice = mydiscount.division(500,20);
	System.out.print("The finalPrice is: " + finalPrice);
	}

}


