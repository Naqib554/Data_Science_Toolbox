# A lambda function is an anonymous function that can be used for simple, one-line operations
# the lamda function add_bangs take one argument a and return a with concatenating 3 sign of exlamation marks.
# this function does not have name .
add_bangs=(lambda a:a+'!!!')
h=add_bangs('hello')
print(h)



# convert the bellow simple function to lamda function.
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words


echo_word=(lambda word1,echo:word1*echo)
result=echo_word('hey',5)
print(result)