# recursion from Lynda.com class
# based on:   n! = n * (n-1)!   for n greater than 1
def factorial(n):
    # return the factorial of positive integer n 
    if n == 1:     # "base case" 1! = 1
        return 1
    else:           # "recursive case"
        return n * factorial(n-1)

print(1,factorial(1))
print(2,factorial(2))
print(3,factorial(3))
    