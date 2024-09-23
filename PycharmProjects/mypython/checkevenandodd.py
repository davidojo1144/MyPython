def check_even_and_odd_count(numbers):
    even = []
    odd = []
    if numbers % 2 == 0:
        even.append(numbers)
        gotten_even = even.count(numbers)
    else :
        odd.append(numbers)
        gotten_odd = odd.count(numbers)

        answer = gotten_even + gotten_odd
        return answer

print(check_even_and_odd_count([2,1,5,7,8]))




