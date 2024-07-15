largest = 0
second_largest = 0

for integers in range(10):
	number = int(input("Enter a number: "))

	if number > largest:
		second_largest = largest
		largest = number
	elif number > second_largest:
		second_largest = number

print("the largest number is:", largest)
print("the second_largest number is:", second_largest)