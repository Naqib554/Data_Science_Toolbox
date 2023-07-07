numbers = [1, 2, 3, 4, 5]
# For the first iteration:

# num is assigned the value 1.
# The key-value pair {1: 1} is created in the dictionary.
# For the second iteration:

# num is assigned the value 2.
# The key-value pair {2: 4} is created in the dictionary.
squared_dict = {num: num**2 for num in numbers}

print(squared_dict)
