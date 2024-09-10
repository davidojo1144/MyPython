def special_characters(input):
    bad_characters = [",", ".", "*", ";", ":", "?", "'"]
    for char in bad_characters:
        input = input.replace(char, "")
    return input

print(special_characters("he,ll.o"))
print(special_characters("da;n:i'e;l"))






def compare(input1, input2):
    name = input1 == input2
    return name

print(compare("david", "david"))





def compare2(input1):
    return input1.count("a")

print(compare2("david"))





def check_index(name):
    return name.index("d", 2)

print(check_index("david"))





def check_elements(name):
    check = "d" in name
    return check

print(check_elements("david"))


def check_starts(name):
    return name.startswith("d")

print(check_starts("david"))








#def word_change(word):
    #if len(word) // 2 == 0:
        #answer = "ce"
       # answer2 = answer

#print(word_change("helloo"))


