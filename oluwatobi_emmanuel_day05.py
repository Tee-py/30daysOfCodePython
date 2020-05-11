"""A python function that prints the nth faithful
number by accepting n as a parameter"""
def faithful(n):
    rev_bin_n = str(bin(n)[2:][::-1])
    total = 0
    for i in range(len(rev_bin_n)):
        total += int(rev_bin_n[i])*(7**i)
    return f'{n}th faithful number: {total}'
#call the function here
n = int(input('Enter the value of n:'))
print(faithful(n))
