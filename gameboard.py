from graphics import *
from menu import *
from mastermind_alg import *

#class for each playable slot
class Pegslot(Circle):
    def __init__(self):
		
        location = 0
    def setColor(self, color):
        self.setFill(color)

#create global playboard which is an 2d list of all playable slots
playboard = [[Pegslot() for i in range(4)] for j in range(12)]
# create global guessboard which is a 2d list of all slots to show correctness
guessboard = [[Pegslot() for i in range(4)] for j in range(12)]

#after the user clicks a color, it will set this variable
activeColor = color_rgb(102, 51, 0)
redPeg = orangePeg = yellowPeg = greenPeg = bluePeg = purplePeg = Pegslot


def functionality(win, e):
    # takes in win (graphic) and e (exit button)
    global activeColor

    # functionality to close window when a button is clicked
    while True:
        mouse = win.getMouse()  # pause for click in "Exit" button
        #check to see if clicked inside of a playable peg slot
        for i in range(12):
            for j in range(4):
                if (playboard[i][j].p1.x < mouse.x and playboard[i][j].p1.y < mouse.y) and\
                        (playboard[i][j].p2.x > mouse.x and playboard[i][j].p2.y > mouse.y):
                    playboard[i][j].setFill(activeColor)
        #check to see if clicked in color selection
        if (redPeg.p1.x < mouse.x and redPeg.p1.y < mouse.y) and\
                        (redPeg.p2.x > mouse.x and redPeg.p2.y > mouse.y):
                    activeColor = 'red'
        if (orangePeg.p1.x < mouse.x and orangePeg.p1.y < mouse.y) and\
                        (orangePeg.p2.x > mouse.x and orangePeg.p2.y > mouse.y):
                    activeColor = 'orange'
        if (yellowPeg.p1.x < mouse.x and yellowPeg.p1.y < mouse.y) and\
                        (yellowPeg.p2.x > mouse.x and yellowPeg.p2.y > mouse.y):
                    activeColor = 'yellow'
        if (greenPeg.p1.x < mouse.x and greenPeg.p1.y < mouse.y) and\
                        (greenPeg.p2.x > mouse.x and greenPeg.p2.y > mouse.y):
                    activeColor = 'green'
        if (bluePeg.p1.x < mouse.x and bluePeg.p1.y < mouse.y) and\
                        (bluePeg.p2.x > mouse.x and bluePeg.p2.y > mouse.y):
                    activeColor = 'blue'
        if (purplePeg.p1.x < mouse.x and purplePeg.p1.y < mouse.y) and\
                        (purplePeg.p2.x > mouse.x and purplePeg.p2.y > mouse.y):
                    activeColor = 'purple'
        #check to see if clicked on exit box
        if e.p1.x < mouse.x < e.p2.x and e.p1.y < mouse.y < e.p2.y:
            win.close()
            break

# sets up board graphics
def board(win):
    # takes in win (graphic) and returns e (exit button)
    global redPeg, orangePeg, yellowPeg, greenPeg, bluePeg, purplePeg

    # actual game board
    r = Rectangle(Point(50, 25), Point(350, 550))
    r.draw(win)
    r.setFill(color_rgb(204, 102, 0))
    # "cover" of the solution at the bottom
    cover = Rectangle(Point(70, 525), Point(210, 550))
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
            playboard[i][j].setFill(color_rgb(102, 51, 0))
            #smaller pegs to indicate correctness of the guess
            if(j == 0):
                guessboard[i][j] = Circle(Point(225, 62 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(102, 51, 0))
            if(j == 1):
                guessboard[i][j] = Circle(Point(225, 48 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(102, 51, 0))
            if(j == 2):
                guessboard[i][j] = Circle(Point(239, 62 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(102, 51, 0))
            if(j == 3):
                guessboard[i][j] = Circle(Point(239, 48 + 40 * i), 5)
                guessboard[i][j].draw(win)
                guessboard[i][j].setFill(color_rgb(102, 51, 0))
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
    # button to submit guess
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
    return e


def main():
    code = generateCode()
    # Initiates the menu
    gameParam = menufunctionality()
    # If the user did not click the quit button in the menu
    if (gameParam.quitting != 1):
        # setting up window for the game
        win = GraphWin("Mastermind", 400, 600)
        # takes the window and creates the board
        # returns the exit button
        e = board(win)
        # the functionality takes in the window and exit button as params
        functionality(win, e)


main()
