numbers = ["2", "3", "9", "5", "6"]
num = [int(number) for number in numbers]
def biggest_odd(numbers):
            odd_numbers = [number for number in num if number % 2 != 0]
            return max(odd_numbers)
            if not odd_numbers:
                return none
print(biggest_odd(numbers))


def equal_strings(string1, string2):
    if sorted(string1) != sorted(string2) and len(string1) != len(string2):
        return False
    else :
        return True
print(equal_strings("love", "evol"))
