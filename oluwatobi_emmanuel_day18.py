"""
A python function that returns true if two numbers passed as arguments are
amicable. i.e The sum of their proper divisors is the same as one of them.
"""

def amicable(num1,num2):
    if str(num1)[0]=='-' or str(num2)[0]=='-':
        return 'The two args should be positive integers'
    else:
        try:
            div_num1 = [num for num in range(1,num1//2+1) if num1%num==0]
            div_num2 = [num for num in range(1,num2//2+1) if num2%num==0]
            if sum(div_num1)==num2 and sum(div_num2)==num1:return True
            else:return False
        except:return 'Argument passed should be an interger e.g is_amicable(12,34)'

print(amicable(-284,220))