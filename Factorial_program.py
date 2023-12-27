# Find factorial of the nunber use recursion 
def Fac(n):
    if n == 1: 
        return n
    else: 
        return n*Factorial(n-1)
'Fac is the function find factorial'