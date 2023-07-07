
gen=(num*2 for num in range(10))

# like any other iterator, we can pass a generator to the function next in order to iterate through its elements.
# This can help a great deal when working with extremely large sequences as you don't want to store the entire list in memory, 
# which is what comprehensions would do; you want to generate elements of the sequence on the fly.
print(next(gen))
print(next(gen))
print(next(gen))
# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))


# Print the rest of the values
for value in result:
    print(value)