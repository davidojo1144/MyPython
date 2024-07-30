
for number in range(1000,3001):
	if number % 2 == 0:
		value_one = number % 10
		value_two = number // 10
		value_three = value_two % 10
		value_four = value_two // 10
		value_five = value_four % 10
		value_six = value_four // 10
		if value_one % 2 == 0 and value_three % 2 == 0 and value_five % 2 == 0 and value_six % 2 == 0 :
			print(number, end=",")	
	