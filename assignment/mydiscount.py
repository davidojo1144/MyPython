price = 500
discount = 20

def my_discount(price, discount):
	discounted_amount = price * (discount / 100)
	final_price = price - discounted_amount
	return final_price
	

result = my_discount(price, discount)
print(result)
