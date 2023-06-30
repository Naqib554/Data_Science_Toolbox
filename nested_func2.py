#closure concept :
 
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# The closure essentially captures the state of the outer_function at the time it was invoked. 
# In this case, it captures the value of x, which is 5, and retains it for later use.
closure = outer_function(5)
result = closure(3)
print(result)  # Output: 8
# print(closure)





# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
