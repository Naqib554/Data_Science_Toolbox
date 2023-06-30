import pandas as pd

dictionary = {
    "languages": ["Python", "JavaScript", "Java", "C++", "C++", "Java"],
    "sources": ["OpenAI", "Mozilla", "Oracle", "Microsoft", "mobile", "amazone"]
}

def funct(df, lang):
    '''The function takes a dataframe as the first parameter and the column name as the second parameter'''

    df = pd.DataFrame(df)
    language_count = {}

    col = df[lang]
    for entry in col:
        if entry in language_count.keys():
            language_count[entry] += 1
        else:
            language_count[entry] = 1

    return language_count

hi = funct(dictionary, 'languages')
hi2 = funct(dictionary, 'sources')

print(hi)
print(hi2)
