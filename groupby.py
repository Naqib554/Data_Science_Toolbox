# Example list of words
words = ["apple", "banana", "cat", "dog", "elephant","ap"]

# Grouping words by their first letter
groups = {}
for word in words:
# For each word, we extract its first letter using indexing (word[0]) and assign it to the variable key.
    key = word[0]
    # print(key)
    if key in groups:
# if the key exist alread in the groups dictionary then append the word value.
        groups[key].append(word)
    else:
        # create a new key in groups dictionary
        groups[key] = [word]
# print(groups)

# # Iterating over groups
for key, group in groups.items():
    print(f"Key: {key}")
    print(f"Group: {group}")
    print()
