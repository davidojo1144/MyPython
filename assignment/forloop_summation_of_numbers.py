
def for_loop_summation(numbers):
	for number in numbers(1,50):
		result = sum(numbers)
	return result

print(for_loop_summation(numbers))