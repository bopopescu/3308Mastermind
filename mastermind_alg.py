# Sonia Szeton
# Functions needed to maintain board
import random
from enum import Enum

# enumerated type to create the colored pegs
class Peg(Enum):
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
        code.append(Peg(random.randrange(7)))
    return code

# Scores guess by comparing guess to code using loops
# Has some bugs when assigning white pins with duplicates
def scoreGuess(guess,code) :
    score = []
    for j in range(4) :
        for k in range(4) :
            if j == k and guess[j] == code[k] :
                score.append(Pin.black)
                break
            elif j != k and guess[j] == code[k]:
                score.append(Pin.white)
                break
    return score    #TODO: need to randomize score

code = generateCode()
guess = generateCode()
score = scoreGuess(guess,code)

print("Code is: ")
print(code)
print("Guess is: ")
print(guess)
print("score is: ")
print(score)
