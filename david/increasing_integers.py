#i prompted user to input three integers
#then compare all integers to arrange it in increasing order


user_Input1 = int(input("Enter an integer: "))
user_Input2 = int(input("Enter an integer: "))
user_Input3 = int(input("Enter an integer: "))

if user_Input1 < user_Input2  and user_Input3:
	print(user_Input1)
elif user_Input2 < user_Input1 and user_Input3:
	print(user_Input2)
elif user_Input3 < user_Input1 and user_Input2:
	print(user_Input3)

print(f"in increasing order{user_Input2} {user_Input3} {user_Input1}")