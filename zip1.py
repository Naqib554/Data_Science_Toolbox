name=['naqib','jasim','aman']
age=[23,34,55]
# create a zip object
res=zip(name,age)
# print(type(res))

# convert the zip object into the list
e_list=list(res)
print(e_list)


# Alternatively, we could use a for loop to iterate over the zip object and print the tuples.
# unpacking the zip object values
for zip1,zip2 in zip(name,age):
    print(zip1,zip2)
    