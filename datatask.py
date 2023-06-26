import pandas as pd

# Twitter data
data = {
    'lang': ['en', 'es', 'en', 'fr', 'en', 'es', 'en']
}

# Create DataFrame from Twitter data
df = pd.DataFrame(data)
# from new import df
# Define count_entries()
def count_entries(naq, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
   
    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(df, 'lang')

# Print the result
print(result)


# thank you so much