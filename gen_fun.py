def funct(n):
    i=0
    while i<n:
        # when we call the function then yield keyword suspend the execution of function ant return the first iteration 
        # value to the caller and then continue the function execution for next iteration and so on till the end of loop iteration.
        yield i
        i+=1
        
res=funct(2)  
# print(res)
for i in res: 
    print(i)     