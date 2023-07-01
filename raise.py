def func(word,pow):
    if pow<0:
        # this is another way to raise error by using the raise ValueError.
        raise ValueError('the pow must be equall or greater than o')
    return word*pow
res=func(word='hagu',pow=-1)
print(res)