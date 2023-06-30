# Global variable
global_var = 5

def my_function():
    # Local variable
    local_var = 10
    
    # Accessing local variable
    print("Local variable inside the function:", local_var)
    
    # Accessing global variable
    print("Global variable inside the function:", global_var)

# Accessing global variable outside the function
print("Global variable outside the function:", global_var)

# Calling the function
my_function()

# As you can see, the local variable is accessible only within the
# function's scope, while the global variable can be accessed both inside and outside the function.