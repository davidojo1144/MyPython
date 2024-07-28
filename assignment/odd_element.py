def odd_element(my_numbers):
	odd_number = [number for number in my_numbers if number % 2 != 0]
	return odd_number

print(odd_element([2, 6, 8, 42, 12, 4, 9, 7, 89, 1]))


