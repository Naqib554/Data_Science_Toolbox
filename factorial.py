def func(n):
    if n<=1:
        return 1
    else:
        # The value of n is multiplied by the result of the recursive call func(n-1)
        return n* func(n-1)
res=func(6)    
print(res)    
