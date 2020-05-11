

import random
def bin_search(lst, a):
    start_index = 0
    end_index = len(lst)-1
    output = False
    while(start_index<=end_index and output==False):
        mid_index = int((start_index+end_index)/2)
        if lst[mid_index] == a:
            output = True
            return 'number at index '+str(mid_index)
            break
        elif a < lst[mid_index]:
            end_index = mid_index-1
        else:
            start_index = mid_index+1
    return output
# call the function here
result = bin_search([1,2,3,5,8,9,15], 18)
#handle what is returned by the function
if result == True:
    print(result)
else:
    print(result)
    print('number not in List')
print(random.shuffle([1,2]))

