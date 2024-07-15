passed = 0
failed = 0
for score in range (1,6):
	score = int(input("Enter student score: "))

	if score >=  45 and score <= 100:
		passed += 1
	elif score < 45:
		failed += 1
print(f"Number of student who passed: {passed}")
print(f"Number of student who failed: {failed}")



