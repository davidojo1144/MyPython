def listing(numbers):
    dict = {}
    for running in numbers:
        num = running * running * running
        dict[running] = num
    return dict
print(listing([1,2,3,4,5]))