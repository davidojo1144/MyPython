#given gravity_rate to be 15%
#i prompted the user to input a number
#i got gravity by multiplying the userinput with gravity rate and dividing it by 100
#after getting the gravity, i added the gravity with userinput to be able to get the total
#after getting the total i used the print function to print out the gravity and the total.

user_Input = int(input("Enter a number: "))

gravity_rate = 15

gravity = (user_Input * gravity_rate) / 100
total = gravity + user_Input

print("The gravity is: ",gravity)
print("The total is: ",total)

