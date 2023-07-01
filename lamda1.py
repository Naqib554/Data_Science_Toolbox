# The main purpose of using map() in the provided code is to apply a specific operation, 
# defined by a lambda function, to each item in the spells list.

# Create a list of strings: spells
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']

# Use map() to apply a lambda function over spells: shout_spells
# this line return the map object. and the next line this object  convert to a list.
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# # Print the result
print(shout_spells_list)