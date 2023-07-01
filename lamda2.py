# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
# this line return the filter object and the next this object convert to a list by list().
# result variable : contains the members that satisfy the condition.
result = filter(lambda member: len(member) > 6, fellowship)
# print(result)
# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)