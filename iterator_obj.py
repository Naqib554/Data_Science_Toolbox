# create an iterator object called google.
google=iter(range(10**100))
print(google)

print(next(google))
print(next(google))
print(next(google))


# create an iterator object called small_value.
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))