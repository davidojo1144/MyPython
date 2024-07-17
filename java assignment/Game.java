import java.util.Random;
import java.util.Scanner;

public class Game{

	public static void main(String...args){

	Scanner scanner = new Scanner(System.in);

	Random rand = new Random();
	int numbers = rand.nextInt(1,100);

	System.out.println("This is a guessing game. \ni'd love you to choose between 1 to 1000.");
	System.out.println("Let start the game.");

	int counter = 0;
	int user = 0;
	String flag = "";

	while(!flag.equalsIgnoreCase("no")){
		System.out.println("Enter a number: ");
		user = scanner.nextInt();

		counter ++;

		if (user > numbers) System.out.println("Too large, Try again!");
		else if (user < numbers) System.out.println("Too small, Try again!");
		
		if (user == numbers && user <=10){
		System.out.print("Congratulations! You have guessed right");
		}

		System.out.print("Press no to stop or yes to continue: \n");
		flag = scanner.next();
	}
		System.out.print("The amount of times attempted is: " + counter);

	}

}


	
	