from math import gcd as hey

def gcd(num1, num2):
    """A python function that returns the greatest common divisors of two integers."""
    if type(num1) != int or type(num2) != int:return 'Args should be integer values only.'
    elif num1 <= 0 or num2 <= 0:return 'Args should be positive integers only'
    else:
        max_arg = max([num1,num2]);min_arg = min([num1, num2])
        common_divisors = [i for i in range(1,max_arg+1) if max_arg%i==0 and min_arg%i==0];return max(common_divisors)

arg_listInit = [23,45,60,98]
arg_listFin = [2,300,120,-16]
for i in range(len(arg_listInit)):
    print(gcd(arg_listInit[i], arg_listFin[i]))