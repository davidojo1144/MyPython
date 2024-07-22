def only_floats(a, b):
 
	if (a, float) and (b, float):
		return 2
	elif (a, float) and (b, not float):
		return 1
	else:
		return 0

results = only_floats(a, b):
print(results)



 