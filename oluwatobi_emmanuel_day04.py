#import the regex module
import re
def is_Nigerian(number):
    #create the nigerian number regex
    num_regex = re.compile(r'^(081|090|070|080)(\d\d\d\d\d\d\d\d)$')
    #check the argument if it matches the regex
    res = num_regex.search(number)
    if res==None:
        print(False)
    else:
        print(True)
#call the function here
is_Nigerian('08045678798')
