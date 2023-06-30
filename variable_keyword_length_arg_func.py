# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")






# my own practice:
def func1(**kwargs):
    '''print keys and values of the dictionary separated by a colon'''
    for key, value in kwargs.items():  # Use the items() method to iterate over the dictionary
        print(key + ":" + str(value))  # Convert the value to a string to concatenate it with the key

func1(name='naqib ullah', age=22, address='hangu')
