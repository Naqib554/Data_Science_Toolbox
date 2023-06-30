import pandas as pd
dictionary = {
    "languages": ["Python", "JavaScript", "Java", "C++","C++","Java"],
    "sources": ["OpenAI", "Mozilla", "Oracle", "Microsoft","mobile","amazone"]
}

def funct(df,lang):

    '''the function that takes tow perameter one as dataframe and the other one is the column of the dataframe'''
    df=pd.DataFrame(dictionary)
    # print(df)
    language_count={}
    col=df[lang]
    # print(col)

    for entry in col:
        if entry in language_count.keys():
            language_count[entry]+=1
        else:
            language_count[entry]=1
    return language_count        

hi=funct(dictionary,lang='languages')
print(hi)



    