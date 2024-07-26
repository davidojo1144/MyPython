from random import randint
def student_learn():

	question_one = randint(1, 5)
	question_two = randint(1, 5)
	counter = 0
	user = int(input(f"How much is {question_one} times {question_two}: "))
	answer = question_one * question_two
	
	while question_one == question_two or question_one != question_two :
		counter += 1

		if user == answer and answer == 20 to 25 :
			return("Very good!")

		elif user == answer and answer == 16 to 19    :
			return("Nice Work!")

		elif user == answer and answer == 11 to 15:
			return("Keep up the good work!")

		elif user != answer and answer < 11 and 9 : 
			return("No. Please try again.")

		elif user != answer and answer < 9 and 5 :
			return("Wrong. Try once more.")

		elif user != answer and answer < 5 and 1 :
			return("No. Keep trying.")



	
print(student_learn())

	

