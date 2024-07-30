def get_sorted_numbers(num1, num2, num3):
		if num1 < num2 and num1 < num3:
			least_num = num1
		elif num2 < num1 and num2 < num3:
			least_num = num2
		else:
			least_num = num3
		if num1 > num2 and num1 > num3:
			max_num = num1
		elif num2 > num1 and num2 > num3:
			max_num = num2
		else:
			max_num = num3
		if num1 != num2 and num1 != num3:
			medium_num = num1
		elif num2 != num1 and num2 != num3:
			medium_num = num2
		else:
			medium_num = num3
		return least_num, medium_num, max_num



print(get_sorted_numbers(15, 11, 55))