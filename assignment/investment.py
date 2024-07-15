amountAtTheEndOfTheYear = 0
year = 30
annualRate = 7
amountInvested = 1000

for number in range (1,30):
	amountAtTheEndOfTheYear = amountInvested * ((1 + (7/100))*number)
	print("amountAtTheEndOfTheYear:", amountAtTheEndOfTheYear)
