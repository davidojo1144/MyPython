accountbalance = 0
deposit = 0
withdrawal = 0
prompt = 0

while prompt != 4:
	prompt = int(input("Enter 1 to deposit, Enter 2 to withdraw, Enter 3 for account balance, Enter 4 to end:   "))

	if prompt == 1:
		deposit = int(input("Enter amount to deposit: "))
		accountbalance += deposit

	elif prompt == 2:
		withdrawal = int(input("Enter amount to withdraw: "))
		if withdrawal > accountbalance:
			print('invalid amount')
		else:
			accountbalance -= withdrawal

	elif prompt ==3:
		print(accountbalance)

	else:
		break 		

	







