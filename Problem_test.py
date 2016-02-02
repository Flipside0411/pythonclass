L=[1, -2, 3.4]

def applyToEach(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])

# applyToEach(L, abs)  output [1, 2, 3.4]
# applyToEach(L, int)  output [1, -2, 3]
applyToEach(L, )
print (L)