word = input("Enter a word: ")
new_word = set(word)
vowel = 0
consonant = 0
counter = 0
for alphabet in new_word:
	if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "U" or alphabet == "A" or alphabet == "E" or alphabet == "I" or alphabet == "O" or alphabet == "U":
		counter = counter + 1
		vowel = vowel + 1
	else:
		consonant = consonant + 1



print("The number of vowel is:", vowel, "and the number of consonant is:", consonant)
print("The number of times attempted is: ", counter)
		