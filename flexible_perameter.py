def sc(*args):
    '''concatenate multiple strings togather '''
    word=''
    for i in args:
        word+=i
    return word

soup=sc('naqib','ullah','jasim') 
# the function return values to that place from where it is called  .
# and then we store it within a variable.  
print(soup)    

