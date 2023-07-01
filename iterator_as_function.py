# create a range object called value.
# range object is an iterable 
values=range(0,5)
print(values)

# use range object as an argument of function in this case values.
rs=list(values)
print(rs)

# use range object as an argument of function .
res=sum(values)
print(res)




# There are also functions that take iterators and iterables as arguments. For example,
# the list() and sum() functions return a list and the sum of elements, respectively.