largest = 0
smallest = 0
sum = 0
product = 1

for number in range (4):
	integer = int(input("Enter an integer: "))

	if (smallest == 0 or integer < smallest):
		smallest = integer
	if (integer > largest):
		smallest = integer
	sum = sum + integer
	average = sum / 4
	product = product * integer

print("sum:",sum)
print("average:", average)
print("smallest:", smallest)
print("largest:", largest)
print("product:", product)

	
	


		