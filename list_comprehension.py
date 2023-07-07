# You know that list comprehensions can be built over iterables.
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
# print the first character of each name in the doctor
new_list=[doc[0] for doc in doctor]
print(new_list)



# write a list comprehension that produces a list of numbers consisting of the squared values of i.
squares = [i**2 for i in range(0,10)]
print(squares)



# nested_list comprehension.
matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)
for row in matrix:
    print(row)