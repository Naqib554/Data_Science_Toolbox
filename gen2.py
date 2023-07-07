# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# create a generator object that you will iterate over to print its values.
length=(len(person) for person in lannister)
print(length)
# iterate the generator object length
for i in length:
    print(i)