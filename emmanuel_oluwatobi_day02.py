"""This is a function that takes in the lenght of desired password as an argument
and provides password suggestions that are alphanumeric and contains both upper and lowercase
letters"""


def pasword_gen(lenght):
    let_lst = ['a','A','6','8','7','c','d','9','e','E','f','F','g','8','h','0','I','i','0','8']
    password = ''
    lenght = int(lenght)
    if lenght>=8:
        import random
        for x in range(lenght):
            password += random.choice(let_lst)
        return str(password)
    else:
        return 'Your password is weak'
#change the argument...it must be of type str
print(pasword_gen('79'))