# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
# execution of inner():The inner function is called three times with the words 'a', 'b', and 'c    
    def inner(word):
# Each time inner is called, it concatenates the input word with '!!!' and returns the resulting string.
        return word + '!!!'
# The return values of the inner function calls are collected in a tuple
    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))
# Finally, the tuple ('a!!!', 'b!!!', 'c!!!') is returned from the three_shouts function.

# Call three_shouts() and print

print(three_shouts('a', 'b', 'c'))