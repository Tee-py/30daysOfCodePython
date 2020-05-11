
def flattenList(lst):
    str_of_lst = str(lst)
    return_lst = []
    for char in str_of_lst:
        if char.isalpha()==True or char.isdecimal() == True:
            return_lst.append(char)
    return return_lst

print(flattenList([[[1,2],[4,5],[[[[8,9]]]]],7]))


