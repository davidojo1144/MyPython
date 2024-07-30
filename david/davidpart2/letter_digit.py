
all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user = input("Enter a name: ")

total_name = 0
total_number = 0

if user in all_letters:
	total_name += 1
 
else:
	total_number += 1

	print(f"LETTERS {total_name} DIGITS {total_number}")


