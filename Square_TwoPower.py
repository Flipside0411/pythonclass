def square(x):
    return x*x

def twopower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x
