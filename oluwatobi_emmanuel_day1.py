

#A function to compare your guessed score and the actual answer
def check_guess(guess):
    correct_res = 25
    if guess<correct_res:
        print('The difference between your guess and the actual value is '+str(abs(guess-correct_res)))
        print('Print guess Higher')
    elif guess>correct_res:
        print('The difference between your guess and the actual value is '+str(abs(guess-correct_res)))
        print('Guess Lower')
    else:
        print('You made the correct guess')

#call the function here
try:
    guess = int(input('Guess my Test score:'))
    check_guess(guess)
except ValueError:
    print('Your guess should be of type int')