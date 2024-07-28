def list_of_digits(number):
	result = [int(digit) for digit in str(number)]
	return result

print(list_of_digits(635248594736))