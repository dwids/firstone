# http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
# DS: Newton’s Method.  Just do 20 iterations and return the answer
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))
        
    return root
a = squareroot(2.0)
print (a, a*a)
