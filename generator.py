# create a generate object 
gen=(num*2 for num in range(10))
# print(gen)
# you can loop the generator object to retrieve the value by generating  the generator expression.
for i in gen:
    print(i)

# you can covert the generator object into the list
res=list(gen)
print(res)







# list comprehension produces a list as output while generator produces a generator objec 
# like any other iterator, we can pass a generator to the function next in order to iterate through its elements.