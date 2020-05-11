'''This is a compressor function that takes in a string of positive integers and
returns a tuple of tuples. Each subtuple consists of a number as its first item and
the number of occureneces in the string as its second item. It also takes care of
possible repetitions in the super tuple. It creates a list of the argument passed
and uses a while loop to count the number of occurences in the list by using the List's
count method. If the count is not equals 1, it adds the count to the loop variable i
so as to shift the index location by the count to avoid repetitions and
if the count is 1 it adds 1 to the count 1 to the loop variable
which indicates that the next element is not the same as the current element. It appends
a tuple of the number and count to and output list and returns a tuple of the output list.'''

def compressor(val):
    try:
        new_val = list(val)
        new_val.sort()
        output_lst = []
        i = 0
        num_lst = []
        while i<len(new_val):
            if new_val.count(new_val[i])!=1:
                num_lst.append(int(new_val[i]))
                num_lst.append(new_val.count(new_val[i]))
                output_lst.append(tuple(num_lst))
                i += new_val.count(new_val[i])
                num_lst = []
            else:
                num_lst.append(int(new_val[i]))
                num_lst.append(new_val.count(new_val[i]))
                output_lst.append(tuple(num_lst))
                i+=1
                num_lst = []
        return tuple(output_lst)
    except:
        return "Invalid argument; argument should be a str of positive integers e.g compressor('12345')"
print(compressor('334433221122111'))

