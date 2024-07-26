from random import randint

print("Guess my number between 1 and 1000 with the fewest guesses:")
user_input = int(input("Enter a number: "))
guess_number = randint(1,1001)
counter = 0

while guess_number != user_input :
	counter += 1
	if user_input < guess_number :
		print("Too low. Try again.")
	elif user_input > guess_number :
		print("Too high. Try again.")

	user_input = int(input("Enter a number: "))

print("Congratulations. You guessed the number!")

if counter <= 10 :
	print("Either you know the secret or you got lucky!")
elif counter > 10 :
	print("You should be able to do better!")




