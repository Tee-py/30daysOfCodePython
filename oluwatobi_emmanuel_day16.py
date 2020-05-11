"""This is a python function that takes in two binary
numbers as parameters and returns the sum of the two
numbers in binary"""

def binary_adder(a,b):
    try: return str(bin(int('0b'+str(a),2)+int('0b'+str(b),2)))[2:];
    except: return 'The two arguments should be a binary number';

import time
now = time.time()*1000
print(binary_adder(11111111111111111111,1111111111111111))



