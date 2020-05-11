"""A python function that find the sum of the first n abundant numbers
"""

def abundant(num):
    if str(num)[0]=='-':
        return 'Argument should be a positive integer'
    else:
        try:
            div_lst = [x for x in range(1,(num//2+1)) if num%x==0]
            if sum(div_lst) > num:return True
            else:return False
        except:
            return 'Argument should be a positive integer'

def sum_abundant(n):
    if type(n)==str or str(n)[0]=='-' or type(n)==float:
        return 'Invalid Argument passed... Argument should be a positive integer'
    else:
        i=1
        result = []
        while i>0:
            if len(result)==n:
                return sum(result)
                break
            else:
                try:
                    if abundant(i)==True:
                        result.append(i)
                        i+=1
                    else:
                        i+=1
                except:return 'Argument passsed should be an integer'

print(sum_abundant(9))
print(abundant('op'))