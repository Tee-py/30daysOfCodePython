"""This is a function created by Emmanuel Oluwatobiloba
that simulates the hangam game by taking a word and number
of trials as an argument and allows users to guess the
letters contained in the word according to the number of
trials. It returns if the user successfully guessed all
the letters or not"""

def Hangam(word, trials):
    try:
        score = 0
        init = len(word)
        hint = '_ '*init
        for i in range(trials):
            print(hint)
            letter = input('Guess any letter in the word: ')
            word = list(word)
            if letter in word:
                print (letter)
                word.remove(letter)
                score += 1
                if len(word)==0:
                    break
            else:
                print('_')
        if score == init:
            return 'You won: You succesfully guessed all the letters in the word'
        else:
            return 'You lost: you have exhausted your trials.'
    except:
        return "Hangam function takes in two parameters: the first is type str and the second is type int e.g Hangam('praise', 5)"

word = 'fish'
trial = len(word)+2
print(Hangam(word, trial))