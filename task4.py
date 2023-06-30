import pandas as pd

dictionary = {
    "languages": ["Python", "JavaScript", "Java", "C++", "C++", "Java"],
    "sources": ["OpenAI", "Mozilla", "Oracle", "Microsoft", "mobile", "amazone"],
    "frameworks": ["Django", "React", "Spring", "Qt", "Qt", "Spring"]
}

def funct(df, *args):
    '''The function takes a dataframe as the first parameter and variable arguments for column names'''

    df = pd.DataFrame(df)
    count_dict = {}

    for col_name in args:
        col = df[col_name]
        for entry in col:
            if entry in count_dict.keys():
                count_dict[entry] += 1
            else:
                count_dict[entry] = 1

    return count_dict

hi = funct(dictionary, 'languages')
hi2 = funct(dictionary, 'languages', 'sources', 'frameworks')

print(hi)
print(hi2)
