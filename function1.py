# Define the function shout
def shout():
    # docstring describes what the function does.
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()




# function_NO_2
def shout1(word):
    # above line called the function header.
    '''function take one str value and then concatenate this value with the  other string value'''
    shout_word1=word+'!!!'
    print(shout_word1)
shout1('hangu')



# function_No_3
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word=word+'!!!'
    # Replace print with return
    return shout_word
# Pass 'congratulations' to shout: yell
yell=shout('pakistan')

# Print yell
print(yell)


# Great work! Here it made sense to assign the output of shout('congratulations') to a variable yell because 
# the function shout actually returns a value, it does not merely print one.