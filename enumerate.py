# enumerate object Contains the iterable values as well as its index value.
name=['naqib','jasim','aman']
# create enumerate object
res=enumerate(name)
print(type(res))

# convert enumerate object into the list
e_list=list(res)
print(e_list)



# enumerate object is also an iterable and we can loop over it while unpacking its elements
# in this case implicitly create enumerate object and then loop over while unpacking its element.
for index,value in enumerate(name):
    print(index,value)
