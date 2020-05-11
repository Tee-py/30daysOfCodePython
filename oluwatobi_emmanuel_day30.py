

def nester(s):
    """A python program that that inserts a minimum number of opening and closing parentheses into s string containing
    numbers such that the resulting string is balanced and each digit d is inside exactly d pairs of matching
    parentheses."""

    #checks if the argument is a string
    if type(s) != str: return 'Invalid args!!... s should be a string'
    try:
        #checks if the chars in the string can be typecasted to integer..
        int(s); S_list = [int(num) * '(' + num + ')' * int(num) for num in str(s)]; S = ''.join(S_list)
        for iter_i in range(9):
            S = S.replace(')(', '')
        return S
    #Inform the user that the argument does not contain numbers
    except: return 'String s should contain numbers only'

print(nester('233'))




