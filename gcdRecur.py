def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    Write a function runs Euclid's algorithm.
    '''
    if b <= 0:
        return a;
    else:
        return gcdRecur(b, a % b);
