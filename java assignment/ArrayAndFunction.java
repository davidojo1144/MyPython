
import java.util.Arrays;
public class ArrayAndFunction{

	public static int[] calculating(int[] integers){

	for(int index = 0; index < integers.length; index++){
		for (int count = index + 1; count < integers.length; count++){
		if(integers[index] > integers[count]){
		integers[index] = integers[index] + integers[count];
		integers[count] =integers[index] - integers[count];
		integers[index] = integers[index] - integers[count];
		}
		}
	}
	return integers;

	}

	public static void main(String...args){
	int [] integers = {1, -20, 7, 6, 1, 8, 3, 0};
	int [] result = calculating(integers);
	System.out.print("The ascending order is: " + Arrays.toString(integers));
	}

}
	

		
	
