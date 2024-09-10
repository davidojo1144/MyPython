tuple2 = ('orange', [10,20,30], (5, 15, 25))
tuple3 = list(tuple2)
print(tuple3)
print(tuple2[1][1], end =" ")
print(tuple2[2][2])
print(tuple2)
tuple3 += tuple2
print(tuple3)

numbers = [1,2,3,4,5,6]
print(8 in numbers)
print(7 in range(len(numbers)))

