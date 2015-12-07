# Sonia Szeton
# Functions needed to maintain board
import random
from enum import Enum

# enumerated type to create the colored pegs
class Peg(Enum):
    """ Defines the class Peg as enumerated type. The pegs will be used to create codes.
        
    """
    matched = -1
    empty = 0
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    purple = 6

# Pins used to score the guess, black=correct color and placement
class Pin(Enum):
    """ Defines the class Pin as enumerated type. The pins will be used to score guesses.

    """
    black = 1
    white = 2

# Generates random code for user to guess
def generateCode(difficulty):
    """ This function makes a code using 4 pegs catered to the user's difficulty prefrence

        :param difficulty: The level of difficulty the user has chosen.
        :type difficulty: int.
        :returns: array containing 4 pegs.

    """
    code = []
    # difficulty Easy - don't want any blanks, or duplicates
    if difficulty == 0 :
        for i in range(4) :
            peg = Peg(random.randrange(1, 7))
            while peg in code :
                peg = Peg(random.randrange(1, 7))
            code.append(peg)
        return code

    # difficulty Medium - don't want any blanks, but allow duplicates
    if difficulty == 1 :
        for i in range(4) :
            peg = Peg(random.randrange(1, 7))
            code.append(peg)
        return code


    # difficulty Hard - allow blanks and duplicates
    if difficulty == 2 :
        for i in range(4) :
            peg = Peg(random.randrange(0, 7))
            code.append(peg)
        return code


# Scores guess by comparing guess to code using loops
def scoreGuess(guess,code) :
    """ Scores the user's guess by comparing it to the real code using loops
        
        :param guess: The user's guess.
        :type guess: array containing 4 guessed pegs.
        :param code: The generated code the user is trying to guess.
        :type code: array containing 4 pegs.
        :returns: array of pins to give the user feedback. 

    """
    guess = guess[:] # copy the guesses since we are going to pull out the matches
    score = []

    for j in range(4) :
        # first check for an exact match
        if code[j] == guess[j] :
            score.append(Pin.black)
            guess[j] = Peg.matched
            continue # Done with this peg index in the code
        # then check for a match in the wrong position
        for k in range(4) :
            # if they do match, we must make sure the guess doesn't also match a
            # future code pin in the same position!
            if code[j] == guess[k] and code[k] != guess[k] :
                score.append(Pin.white)
                guess[k] = Peg.matched
                break # Done with this peg index in the code

    return score

