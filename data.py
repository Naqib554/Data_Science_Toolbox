import pandas as pd

# Twitter data
data = {
    'lang': ['en', 'es', 'en', 'fr', 'en', 'es', 'en']
}

# Create DataFrame from Twitter data
df = pd.DataFrame(data)

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:
    # if the language is already exist in the langu_count dictionary then increase its value by 1.
    if entry in langs_count:
        langs_count[entry] += 1
    # Else add the language as a key in the to langs_count dictionary & set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
