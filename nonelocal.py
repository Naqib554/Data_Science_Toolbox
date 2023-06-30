# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word=word*2
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        # nonlocal echo_word - This line declares that the variable
        #  echo_word being referenced within the shout function is not local
        #  to the function but refers to the variable defined in the outer echo_shout function.
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word+'!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
print(echo_shout('hello'))