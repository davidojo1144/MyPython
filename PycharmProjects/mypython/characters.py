def check_characters(name):
    check = {}
    for cha in (name):
        check[cha] = name.count(cha)
    return check

print(check_characters("olamide"))


