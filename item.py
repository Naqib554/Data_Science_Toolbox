# Example dictionary
fruits = {'apple': 3, 'banana': 5, 'orange': 2}

# Iterating over key-value pairs using items()
for fruit, quantity in fruits.items():
    print(f"We have {quantity} {fruit}s.")



# in for loop the first variable is initialized by the key of dictionary and 
# the second variable is initialized by that key value in each iteration.


# In this example, items() is called on the fruits dictionary. 
# The loop iterates over the key-value pairs, and in each iteration, 
# the current key is assigned to the variable fruit,
# and the corresponding value is assigned to the variable quantity. 
# This allows you to conveniently access both the key and the value of each item in the dictionary.


# By using the items() method, you can access both the keys and the corresponding values of a dictionary simultaneously within a loop. Each key-value pair is returned as a
# tuple, which can be unpacked into separate variables, typically using a for loop.