# Create a list of strings: flas
# the for loop creates an iterator object and calls the next()
#  function behind the scenes.
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# the actual process of for loop for creating the iterator object and next function is given bellow.
# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))



















# "iterating over a list," 
# it means that we are going through each element or item in the list one by one.
# we can iterate over list using for loop to print each element of a list.
# In simpler terms, an iterable is like a container that holds a collection of items, 
# while an iterator is like a pointer or cursor that allows you to access those items one by one. 
# An iterable provides an iterator to traverse its elements, and the
# iterator remembers its position and knows how to retrieve the next element in the sequence.
