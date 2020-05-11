
def key_pressed(text):
    """A python function that takes in a string argument and returns the number of keypresses to type the string."""
    if type(text) != str:
        return 'Invalid arg!! argument should be a str'
    number_dict = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV',
                   9: 'WXYZ', 0: ' '}
    key_presses = ''
    for char in text.upper():
        try: int_val = int(char); return 'Char must be integer... text must not contain numbers.'
        except:
            for num in number_dict.keys():
                if char in number_dict[num]: key_presses += str(num)*(list(number_dict[num]).index(char)+1)
    return key_presses

print(key_pressed('Hello, World!?'))
print(key_pressed('University Of Ibadan. The First and the Best.'))