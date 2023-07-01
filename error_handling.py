# if you give the wrog argument to the function then it rise the error.and solve the error easily by error_handling concept.
def func(word,pow=1):
    '''function take two argument and then concatenates the strings '''
    word1=''
    word2=''

    # if error is occured then code jump to the except block and print the error message
    # and if the error is not occured then ther try block is executed.
    try:
        # the string and int are not concatenate even you are not change its type.
        word1=word*pow
        word2=word*pow
    except:
        print('the word must be string and pow is integer')
    return word2    


res=func(word='naqib',pow=4)
print(res)





# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")





