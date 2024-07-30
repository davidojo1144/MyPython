user = int(input("Enter an integer: "))
def even_and_odd():
	if user % 2 == 0:
		return("It is an even number")
	if user % 2 != 0:
		return("It is an odd number")

print(even_and_odd())