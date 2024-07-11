import java.util.Scanner;

public class Bank{
	
	public static void main(String...args){

	Scanner input = new Scanner(System.in);
	
	int accountbalance = 0;
	int withdrawal = 0;
	int deposit = 0;
	int prompt = 0;

	while (prompt != 4){
	System.out.println("Enter 1 to deposit, Enter 2 to withdraw, Enter 3 for account balance, Enter 4 to end:   ");
	prompt = input.nextInt();
	

	if (prompt == 1){
	System.out.println("Enter amount to deposit: ");
	deposit = input.nextInt();
	accountbalance += deposit;
	}

	else if (prompt == 2){
	System.out.println("Enter amount to withdraw: ");
		if (withdrawal > accountbalance)
		System.out.println("invalid amount");
		else 
		accountbalance -= withdrawal;
	}

	else if (prompt ==3){
	System.out.print(accountbalance);
	}

	else{
		break;	
	}

	}
}
}	


	
	




	



	
	

