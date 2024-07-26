def get_product(*digit):
	product = 1
	for number in digit:
		product *= number
	return product

print(get_product(1, 4, 5))
print(get_product(1, 4, 7, 9, 10))


	