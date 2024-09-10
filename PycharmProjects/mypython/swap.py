def swapping_two_strings(name1, name2):
    name1 = "abc".replace("c", "z")
    name2 = "xyz".replace("z", "c")
    answer = name2 + name1
    return answer

print(swapping_two_strings("abc", "xyz"))




def upper_before_lower(word):
    global answer
    upper = ""
    lower = ""
    for letter in word:
        if letter.isupper():
            upper += letter

        elif letter.islower():
                lower += letter

                answer = upper + lower
    return answer

print(upper_before_lower("ChAracTERISticS"))




def word_character(input1, input2):
    result = input1.count("o")
    return input2, result

print(word_character("semicolon", "o"))





def adding_ce(word):
    length = len(word)
    middle_index = length // 2

    if length % 2 != 0:
        return word + "ce"
    else:
        return word[:middle_index] + "ce" + word[middle_index:]

print(adding_ce("helloo"))
print(adding_ce("world"))
print(adding_ce("even"))






