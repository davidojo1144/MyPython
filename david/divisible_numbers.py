#i prompted user to enter an integer
#then i compare the integers to see if the are divisible by 5 and 6.



user = int(input("Enter an integer: "))
if user % 5 == 0 and user % 6 != 0:
	print("False") 
if user % 5 == 0 or user % 6 == 0:
	print("True") 
if user % 5 == 0 or user % 6 != 0:
	print("but not both? True") 






