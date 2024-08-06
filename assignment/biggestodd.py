number_str = ["2", "3", "4", "6", "8", "9", "10", "11"]
number_int = [int(number) for number in number_str]

def biggest_odd(number_int):
	odd_number = [number for number in number_int if number % 2 != 0]
	return max(odd_number)
	if not odd_number:
		return none

result = biggest_odd(number_int)
print(result)
	
 