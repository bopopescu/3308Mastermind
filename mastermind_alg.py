# Sonia Szeton
# Functions needed to maintain board
import random
from enum import Enum

# enumerated type to create the colored pegs
class Peg(Enum):
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
    black = 1
    white = 2

# Generates random code for user to guess
def generateCode():
    code = []
    for i in range(4) :
        code.append(Peg(random.randrange(1, 7)))
    return code

# Scores guess by comparing guess to code using loops
def scoreGuess(guess,code) :
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

