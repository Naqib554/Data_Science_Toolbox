# zip(), which takes any number of iterables and returns a zip and return a zip object.
#  If you wanted to print the values of a zip object, you can convert it into a list and then print it. 
# Create a list of strings: mutants
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']

# Create a list of strings: aliases
aliases = ['Professor X', 'Iceman', 'Nightcrawler', 'Magneto', 'Shadowcat']

# Create a list of strings: powers
powers = ['Telepathy', 'Cryokinesis', 'Teleportation', 'Magnetokinesis', 'Intangibility']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
# print(mutant_data)

# # Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# # Print the zip object
print(mutant_zip)

# # Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
