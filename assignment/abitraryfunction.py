def product_of_integers(*numbers):
	product = 1
	for digit in numbers:
		product *= digit
	return product

print(product_of_integers(1, 5, 7))
print(product_of_integers(2, 8, 7, 6, 45))
print(product_of_integers(8, 7, 7, 2))
	
	
	