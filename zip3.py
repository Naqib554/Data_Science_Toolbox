name = ['naqib', 'jasim', 'aman']
age = [23, 34, 55]

# create a zip object
res = zip(name, age)

# print the zipped values
print(*res)

# create a new zip object or convert the existing zip object to a list
res = list(zip(name, age))

# unzip the zipped values and assign the result to res1, res2
res1, res2 = zip(*res)
print(res1)
print(res2)



