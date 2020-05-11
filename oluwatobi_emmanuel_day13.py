"""This is a function named wrapper that takes in a text and the number of characters to
be printed per line and returns the wrapped text.
"""

def wrapper(text, n):
    #check if the second argument is a negative integer
    if str(n)[0]=='-':
        print('Second argument should be a positive integer')
    else:
        try:
            start_index = 0
            init_n = n
            printed_text = ''
            while True:
                if len(text)-len(printed_text)==0:
                    break
                elif len(text)-len(printed_text)<n:
                    print(text[start_index:])
                    break
                else:
                    print(text[start_index:init_n])
                    printed_text += text[start_index:init_n]
                    start_index+=n
                    init_n += n
        except:
            print("Invalid arguments passed to the wrapper function. First argument should be of type str and second argument an integer e.g wrapper('otedola', 4)")
wrapper(r"Mustapha is a very hardworking Engineering student and this is e\nvident in his results as he is the scholar of the Department of Electrical Electronics Engineering, University of Ibadan.",10)
