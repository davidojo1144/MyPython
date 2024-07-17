from random import randint

print("Guess my number between 1 and 1000 with the fewest guesses")
print("Lets start this game")
user = int(input("Guess a number: ")) 
random_number = randint(1,1001)
counter = 0
stop =""
 
while stop != "yes":
	while user != random_number:
		counter += 1
		if user > random_number:
			print("Too high. Try again")
		elif user < random_number:
			print("Too low. Try again")
		
		user = int(input("Guess a number: ")) 

	print("Congratulations. You guessed the number!")
	print("Number of guesses attempted is: ", counter)
	stop = input("press yes! to stop playing or no! to continue the game: ")
