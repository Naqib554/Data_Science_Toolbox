def count(file,word):
    with open(file) as text:
        file1=text.read()
    words=file1.count(word)
    print("the word {} is appear in {} times ".format(word,words))
count(file='tweets.csv',word='English')    

