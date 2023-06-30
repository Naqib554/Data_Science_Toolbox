# To format strings in Python, you can use the format()

name = "Alice"
age = 25

# Basic formatting
print("My name is {} and I am {} years old.".format(name, age))

# Specifying positions
print("My name is {0} and I am {1} years old.".format(name, age))

# Specifying keywords
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# Specifying variable names
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
