from random import randint
def student_learn():

	question_one = randint(1, 9)
	question_two = randint(1, 9)
	user = int(input(f"How much is {question_one} times {question_two}: "))
	answer = question_one * question_two

	if user == answer :
		return("Very good!")

	elif user != answer :
		return("No. Please try again.")

	
print(student_learn())

	

