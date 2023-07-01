# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
# enumerate(mutants) create enumerate object and then by list() it is coverted to list.
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
# This loop iterates over the mutants list using the enumerate() function.
# It assigns each index to the variable index1 and each value to the variable value1
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)


