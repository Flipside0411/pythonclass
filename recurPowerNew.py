def recurPowerNew(base, exp):
    ''' base: int or float.  exp: int >= 0
    returns: int or float,
    base'''
    if exp <= o:
        return base
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base*recurPowerNew(base, exp-1)
