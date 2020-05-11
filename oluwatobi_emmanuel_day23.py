"""
A python function that accepts a starting number and ending number and prints
anagrams between the interval.
"""

def is_armstrong(num):
    lst = [int(i)**3 for i in str(num)]
    if sum(lst)==num:return True
    else:return False

def find_Armstrong(start, end):
    if type(start)!=int or type(end)!=int or start<0 or end<0:return 'Args should be positive integers not string or float'
    elif start>end:
        return 'Start should be lesser than end value'
    else:
        try:armstrongs = [num for num in range(start, end) if is_armstrong(num)==True];return armstrongs
        except:return 'Invalid Args; args should be positive integers only'

print(find_Armstrong(34, 19))