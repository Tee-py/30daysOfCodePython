"""
A fibonacci function that returns the nth fibonacci number by accepting
an argument n.
"""

def Fibonacci(n):
    if type(n)==str:
        return 'Invalid argument: Argument should be a positive integer'
    elif n<0:
        return 'Invalid argument: Argument should be a positive integer'
    elif n==1:return 0
    elif n==2 or n==3:return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(5))