import math
number = 25

def divide_or_square(number):
	if number % 5 == 0 :
		result = math.sqrt(number)
		return result
	else:
		result2 = number % 5
		return result2

results = divide_or_square(number)
print(results)




