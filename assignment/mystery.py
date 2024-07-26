def mystery(number):
 	digit = 0
 	for value in number:
 		digit += value ** 2
 	return digit

print("The digit is: ", mystery([1, 2, 3, 4, 5]))
