from graphics import *
from menu import *
from mainmind_alg import *
from users import *
from database import *
from scoresystem import *

#class for each playable slot
class Pegslot(Circle):
    """ Class for each playable slot
    
    """
    def __init__(self):
		
        location = 0
    def setColor(self, color):
        self.setFill(color)

#create global playboard which is an 2d list of all playable slots
playboard = [[Pegslot() for i in range(4)] for j in range(12)]
# create global guessboard which is a 2d list of all slots to show correctness
guessboard = [[Pegslot() for i in range(4)] for j in range(12)]
# keep track of colors of each guess
guesscolor = ["", "", "", ""]

#after the user clicks a color, it will set this variable
activeColor = color_rgb(102, 51, 0)
redPeg = orangePeg = yellowPeg = greenPeg = bluePeg = purplePeg = Pegslot


# Window displayed to tell player they won
# Also displays username, score for this game, and high score
def winnerwindow(win, code, cover, winorlose, user, checknum):
    """ Displays window telling user they won and shows their username, score, and high score
    
    :param win: Current gameboard -- what we draw everything to.
    :type win: GraphWin
    :param code: Code user is trying to guess.
    :type code: array.
    :param cover: Green panel covering code.
    :type cover: Graphics Rectangle.
    :param winorlose: Says win or lose.
    :type winorlose: string.
    :param user: The name of the user.
    :type user: string.
    :param checknum: Keeps track of which try they're on.
    :type checknum: integer.
    :returns: re -- restart.
    
    """
    score = score2num(checknum, user.difficulty)
    strscore = str(score)
    w = Rectangle(Point(100, 125), Point(300, 325))
    w.draw(win)
    w.setFill('white')
    if winorlose == 'win':
        winner = Text(Point(200, 225), """
Winner Winner Chicken Dinner
Username: """ + user.name + """
Score: """ + strscore + """
High Score: """ + str(user.highScore) + """
""")
    elif winorlose == 'lose':
        winner = Text(Point(200, 225), """
Better Luck Next Time
Username: """ + user.name + """
Score: 0
High Score: """ + str(user.highScore) + """
""")
    user.newScore(score)
    addHighScoreToDB(user, score)
    winner.setStyle('bold')
    winner.draw(win)
    re = Rectangle(Point(160, 275), Point(240, 295))
    re.draw(win)
    re.setFill('black')
    ret = Text(Point(200, 285), 'Restart')
    ret.draw(win)
    ret.setFill('white')

    # Make the "cover" covering the code come back
    cover.undraw()
    coversliv = Rectangle(Point(70, 515), Point(210, 520))
    coversliv.draw(win)
    coversliv.setFill(color_rgb(0, 153, 76))
    # Display target code where cover was
    answer = revnumguess(code)
    w1 = Circle(Point(80, 537), 10)
    w1.draw(win)
    w1.setFill(answer[0])
    w2 = Circle(Point(120, 537), 10)
    w2.draw(win)
    w2.setFill(answer[1])
    w3 = Circle(Point(160, 537), 10)
    w3.draw(win)
    w3.setFill(answer[2])
    w4 = Circle(Point(200, 537), 10)
    w4.draw(win)
    w4.setFill(answer[3])
    return re

# Convert guess list of strings to "Peg" format used in mainmind_alg code

def numguess(guesscolor):
    """ Converts guess list of strings to Peg format used in mainmind_alg file
    
    :param guesscolor: List of strings with the colors. 
    :type guesscolor: list.
    :returns: list.
    
    """
    newguess = []
    for j in range(len(guesscolor)):
        if guesscolor[j] == 'red':
            newguess.append(Peg.red)
        elif guesscolor[j] == 'orange':
            newguess.append(Peg.orange)
        elif guesscolor[j] == 'yellow':
            newguess.append(Peg.yellow)
        elif guesscolor[j] == 'green':
            newguess.append(Peg.green)
        elif guesscolor[j] == 'blue':
            newguess.append(Peg.blue)
        elif guesscolor[j] == 'purple':
            newguess.append(Peg.purple)
        else:
            newguess.append(Peg.empty)
    return newguess

def revnumguess(code):
    """ What this function does
    
    :param code: Code the user is trying to guess. 
    :type code: list.
    :returns: list.
    
    """
    newcode = []
    for j in range(len(code)):
        if code[j] == Peg.red:
            newcode.append('red')
        elif code[j] == Peg.orange:
            newcode.append('orange')
        elif code[j] == Peg.yellow:
            newcode.append('yellow')
        elif code[j] == Peg.green:
            newcode.append('green')
        elif code[j] == Peg.blue:
            newcode.append('blue')
        elif code[j] == Peg.green:
            newcode.append('green')
        elif code[j] == Peg.purple:
            newcode.append('purple')
        else:
            newcode.append('')
    return newcode


# takes the score and sets the small pegs to indicate correctness
# black peg: correct color and placement
# white peg: correct color, wrong placement
def setscore(score, checknum):
    """ Takes the score and sets the pins to indicate correctness. Black is right color and placement. White is right color, wrong placement.
    
    :param score: List from scoreGuess that will get translated to the graphics.
    :type score: list.
    :param checknum: The number of guesses the user has checked.
    :type checknum: integer.
    :returns: black -- number of black pins.
    
    """
    black = 0
    for j in range(len(score)):
        if score[j] == Pin.black:
            guessboard[12 - checknum][j].setFill("black")
            black = black + 1
        else:
            guessboard[12 - checknum][j].setFill("white")
    return black

def functionality(win, e, b, code, cover, user):
    # takes care of all the "button" functionality
    # takes in win (graphic), e (exit button),
    #    b (check button), code (code to be guessed)
    """ Handles all the button functionality
    :param win: Current gameboard things are being drawn to.
    :type win: GraphicWin.
    :param e: The exit button.
    :type e: Graphics Rectangle.
    :param b: Check button.
    :type b: Graphics Rectangle.
    :param code: Code to be guessed.
    :type code: list.
    :param cover: Green panel covering the code on the game board.
    :type cover: Graphics Rectangle.
    :param user: User's name.
    :type user: string.
    :returns: None. 
    
    """
    global activeColor
    checknum = 1
    won = False
#    pointUpdate(win, checknum)

    # tracks currently selected peg
    activePeg = redPeg

    # functionality to close window when a button is clicked
    while True:
        mouse = win.getMouse()  # pause for click in "Exit" button
        for j in range(4):
            # one of the playable pegs is clicked
            if (playboard[12 - checknum][j].p1.x < mouse.x and playboard[12 - checknum][j].p1.y < mouse.y) and\
                    (playboard[12 - checknum][j].p2.x > mouse.x and playboard[12 - checknum][j].p2.y > mouse.y):
                # changing color of peg on board
                playboard[12 - checknum][j].setFill(activeColor)
                # change color in guess list
                guesscolor[j] = activeColor

        #check to see if clicked in color selection
        # if color selection is clicked, activeColor variable = color  
        if (redPeg.p1.x < mouse.x and redPeg.p1.y < mouse.y) and\
                        (redPeg.p2.x > mouse.x and redPeg.p2.y > mouse.y):
                    activePeg.setWidth(1)
                    activePeg = redPeg
                    activeColor = 'red'
                    activePeg.setWidth(3)
        if (orangePeg.p1.x < mouse.x and orangePeg.p1.y < mouse.y) and\
                        (orangePeg.p2.x > mouse.x and orangePeg.p2.y > mouse.y):
                    activePeg.setWidth(1)
                    activePeg = orangePeg
                    activeColor = 'orange'
                    activePeg.setWidth(3)
        if (yellowPeg.p1.x < mouse.x and yellowPeg.p1.y < mouse.y) and\
                        (yellowPeg.p2.x > mouse.x and yellowPeg.p2.y > mouse.y):
                    activePeg.setWidth(1)
                    activePeg = yellowPeg
                    activeColor = 'yellow'
                    activePeg.setWidth(3)
        if (greenPeg.p1.x < mouse.x and greenPeg.p1.y < mouse.y) and\
                        (greenPeg.p2.x > mouse.x and greenPeg.p2.y > mouse.y):
                    activePeg.setWidth(1)
                    activePeg = greenPeg
                    activeColor = 'green'
                    activePeg.setWidth(3)
        if (bluePeg.p1.x < mouse.x and bluePeg.p1.y < mouse.y) and\
                        (bluePeg.p2.x > mouse.x and bluePeg.p2.y > mouse.y):
                    activePeg.setWidth(1)
                    activePeg = bluePeg
                    activeColor = 'blue'
                    activePeg.setWidth(3)
        if (purplePeg.p1.x < mouse.x and purplePeg.p1.y < mouse.y) and\
                        (purplePeg.p2.x > mouse.x and purplePeg.p2.y > mouse.y):
                    activePeg.setWidth(1)
                    activePeg = purplePeg
                    activeColor = 'purple'
                    activePeg.setWidth(3)

        # check to see if check box is clicked
        if b.p1.x < mouse.x < b.p2.x and b.p1.y < mouse.y < b.p2.y:
            newguess = numguess(guesscolor)
            score = scoreGuess(newguess, code)
            black = setscore(score, checknum)
            if(black == 4):
                re = winnerwindow(win, code, cover, 'win', user, checknum)
                won = True

            if(checknum == 12):
                re = winnerwindow(win, code, cover, 'lose', user, checknum)
                won = True    

            checknum = checknum + 1
 #           pointUpdate(win, checknum)

        #check to see if clicked on exit box
        if e.p1.x < mouse.x < e.p2.x and e.p1.y < mouse.y < e.p2.y:
            win.close()
            break
        if won == True:
            if re.p1.x < mouse.x < re.p2.x and re.p1.y < mouse.y < re.p2.y:
                win.close()
                main()

# sets up board graphics
def board(win, user):
    # takes in win (graphic) and returns e (exit button)
    """ Sets up the board graphics
    
    :param win: Current gameboard things are drawn to.
    :type win: GraphicWin.
    :param user: Name of the user.
    :type user: string.
    :returns: e, b, and cover to see if needs to exit, check, or show code by taking away cover.
    
    """
    global redPeg, orangePeg, yellowPeg, greenPeg, bluePeg, purplePeg

    # actual game board
    r = Rectangle(Point(50, 25), Point(350, 550))
    r.draw(win)
    r.setFill(color_rgb(204, 102, 0))

    # "cover" of the solution at the bottom
    cover = Rectangle(Point(70, 515), Point(210, 550))
    cover.draw(win)
    cover.setFill(color_rgb(0, 153, 76))

    # loops to make all of the peg holes on the board
    i = 0
    while i < 12:
        j = 0
        while j < 4:
            # bigger pegs to put guesses in
            playboard[i][j] = Circle(Point(80 + 40 * j, 55 + 40 * i), 10)
            playboard[i][j].draw(win)
            playboard[i][j].setFill(color_rgb(145, 93, 0))

            #smaller pegs to indicate correctness of the guess
            if(j == 0):
                guessboard[i][j] = Circle(Point(225, 62 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(145, 93, 0))
            if(j == 1):
                guessboard[i][j] = Circle(Point(225, 48 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(145, 93, 0))
            if(j == 2):
                guessboard[i][j] = Circle(Point(239, 62 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(145, 93, 0))
            if(j == 3):
                guessboard[i][j] = Circle(Point(239, 48 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(145, 93, 0))
            j = j + 1
        i = i + 1

    # peg options to the left of the holes
    redPeg = Circle(Point(280, 490), 10)
    redPeg.draw(win)
    redPeg.setFill('red')
    orangePeg = Circle(Point(310, 490), 10)
    orangePeg.draw(win)
    orangePeg.setFill('orange')
    yellowPeg = Circle(Point(280, 460), 10)
    yellowPeg.draw(win)
    yellowPeg.setFill('yellow')
    greenPeg = Circle(Point(310, 460), 10)
    greenPeg.draw(win)
    greenPeg.setFill('green')
    bluePeg = Circle(Point(280, 430), 10)
    bluePeg.draw(win)
    bluePeg.setFill('blue')
    purplePeg = Circle(Point(310, 430), 10)
    purplePeg.draw(win)
    purplePeg.setFill('purple')

    # button to check guess
    b = Rectangle(Point(270, 340), Point(320, 360))
    b.draw(win)
    b.setFill('white')
    b2 = Text(Point(295, 350), "Check")
    b2.draw(win)

    # button to exit the window
    e = Rectangle(Point(270, 50), Point(320, 70))
    e.draw(win)
    e.setFill('white')
    e2 = Text(Point(295, 60), "Exit")
    e2.draw(win)

    # Box for displaying username on gameboard
    userName = Text(Point(295, 80), "User: " + user.name)
    userName.draw(win)
    scoreBoard = Text(Point(295, 100), "High Score: " + str(user.highScore))
    scoreBoard.setSize(9)
    scoreBoard.draw(win)

    # Box for displaying difficulty setting on gameboard
    dif = ""
    if user.difficulty == 0:
        dif = "Easy"
    elif user.difficulty == 1:
        dif = "Medium"
    elif user.difficulty == 2:
        dif = "Hard"
    diff = Text(Point(295, 120), "Difficulty: " + dif)
    diff.setSize(9)
    diff.draw(win)

    return (e, b, cover)

def loadHighScore(user):
    """ Goes to database and finds the user's high score 
    
    :param user:
    :type user:
    :returns: int -- the user's high score.
    
    """
    scores = open("scores.csv", 'r')
    highScore = 0
    for line in scores:
        userInfo = line.split(',')
        if userInfo[0] == user:
            for i in range(1,len(userInfo)):
                currScore = int(userInfo[i])
                if currScore > highScore:
                    highScore = currScore
    return highScore

def main():
    # Initiates the menu
    gameParam = menufunctionality()

    # generates new random code
    code = generateCode(gameParam.difficulty)
    print(code)

    # If the user did not click the quit button in the menu
    if (gameParam.quitting != 1):
        user = User(gameParam.user)
        # setting up window for the game
        win = GraphWin("Mainmind", 400, 600)
        # takes the window and creates the board
        # returns the exit an check buttons
        (e, b, cover) = board(win, user)
        functionality(win, e, b, code, cover, user)

main()
