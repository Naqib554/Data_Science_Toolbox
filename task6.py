import pandas as pd

dictionary = {
    "languages": ["Python", "JavaScript", "Java", "C++", "C++", "Java"],
    "sources": ["OpenAI", "Mozilla", "Oracle", "Microsoft", "mobile", "amazone"]
}

def count_occurrences(df, column):
    '''
    A function that takes a DataFrame and a column name as parameters and counts the occurrences of each unique entry in that column.
    '''
    try:
        language_count = {}
        col = df[column]

        for entry in col:
            if entry in language_count:
                language_count[entry] += 1
            else:
                language_count[entry] = 1

        return language_count

    except KeyError as e:
        print(f"Error: Column '{column}' does not exist in the DataFrame.")
        return {}

df = pd.DataFrame(dictionary)

# Example usage
result = count_occurrences(df, column='lang')
print(result)
