def score(numbers):
    verify = [number for number in numbers]
    return min(verify), max(verify)

print(score([2,3,6,7,8]))
print(score([5,3,6,9,8]))


def min_and_max(param):
    return None