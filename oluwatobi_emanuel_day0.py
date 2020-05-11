#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tecra Owner
#
# Created:     29/03/2020
# Copyright:   (c) Tecra Owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
def word_score(letter):
    #dictionary of all letters and their score
    score_dict = {1:['A','E', 'I','L', 'N', 'O', 'R', 'S', 'T'],
    2:['D', 'G'], 3:['B', 'C', 'P'],
    4:['F', 'H', 'V', 'Y'], 5:['K'],
    8:['J','X'], 10:['Q', 'Z']}

    score = 0
    for key, values in score_dict.items():
        for char in letter:
            char = char.upper()
            if char in values:
                score += key
            else:
                score = score

    print(score)

#Call the function here
try:
    word_score('Tee')
except NameError as e:
    print("The argument is to be passed in a '' e.g word_score('letters') ")
