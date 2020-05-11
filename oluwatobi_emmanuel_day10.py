"""This is a function named sieve of eratos written by Emmanuel Oluwatobi that
accepts an integer limiting value n as a parameter and returns a list of prime
number less than the limiting value"""


def sieve_of_eratos(n):
    base_prime = [2,3,5,7]
    num_lst = []
    if str(n)[0]=='-':
        return 'invalid limiting value; limiting value n should be a positive integer'
    else:
        try:
            for i in range(2,n):
                num_lst.append(i)
            for p in base_prime:
                for k in range(len(num_lst)):
                    q = num_lst[k]
                    if p==q:
                        num_lst == num_lst
                    elif (num_lst[k]%p)==0:
                        num_lst[k] = 0
                    else:
                        num_lst[k]==num_lst[k]
            output_lst = []
            for val in num_lst:
                if val!=0:
                    output_lst.append(val)
            return output_lst
        except:
            return 'The limiting value n should be of type int e.g sieve_of_eratos(5)'
print(sieve_of_eratos(60))