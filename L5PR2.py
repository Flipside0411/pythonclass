def recurPower(base, exp):
    ''' base: int or float.  exp: int >= 0
    returns: int or float,  base^exp '''
    if exp <= o:
        return 1
    return base*recurPower(base, exp-1)
