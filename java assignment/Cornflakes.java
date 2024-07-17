import java.util.Scanner;
public class Cornflakes{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int number = scanner.nextInt();
	int result = 0;
	int count = 0;

	for (count = 1; count <= 10; count++){
		result = number * count;
	System.out.printf("%d x %d = %d%n", number, count, result);

	}

	}

}

	

	