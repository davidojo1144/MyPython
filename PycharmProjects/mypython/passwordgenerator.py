import random
import string

def password():
    passcode = []
    for index in range(4):
        random_letter = random.choice(string.ascii_lowercase)
        random_upper = random.choice(string.ascii_uppercase)
        random_symbol = random.choice(string.punctuation)
        random_number = random.randrange(0, 9)
        random_number = str(random_number)
        random_number = random_letter + random_upper + random_symbol + random_number
        passcode.append(random_number)
    passcode = ''.join(passcode)
    return passcode




print(password())