def func1():
    x=10

    def inner():
        # encapsolation mean that the inner function is hide function and the func1 x variable 
        # is accessable within the inner function.
        y=20
        res=x+y
        return res
    return inner()
print(func1())




