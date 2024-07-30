
def reverse(number):
	value_one = number % 10
	value_two = number // 10
	value_three = value_two % 10
	value_four = value_two // 10
	result = str(value_one) + str(value_three) + str(value_four)
	return result



def palindrome(number):
	value_one = number % 10
	value_two = number // 10
	value_three = value_two % 10
	value_four = value_two // 10

	if value_one == value_four:
		return True

	if value_one != value_four:
		return False

print(reverse(456))
print(palindrome(787))



	
	