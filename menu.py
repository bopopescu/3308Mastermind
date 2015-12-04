from graphics import *

class GameParam():
    def __init__(self):
        self.user = 'default'
        self.difficulty = 1
        self.quitting = 0
    def setUser(self, user):
        self.user = user
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty
    def setQuitting(self):
        self.quitting = 1

def menufunctionality():
    # Creates separate GraphWin object for menu
    menu = GraphWin("Main Menu", 400, 600)
    
    # Sets up title
    title = Text(Point(200, 75), 'Mastermind')
    title.setSize(36)
    title.setStyle('bold')
    title.draw(menu)

    # Sets 'warned' as a local variable of menufunctionality()
    warned = 0

    # Sets up buttons
    one = Rectangle(Point(100, 140), Point(300, 210))
    one.draw(menu)
    oneText = Entry(Point(200, 175), 20)
    oneText.setText('Enter username here')
    oneText.draw(menu)
    two = Rectangle(Point(100, 250), Point(300, 320))
    two.draw(menu)
    twoText = Text(Point(200, 285), 'Start')
    twoText.draw(menu)
    three = Rectangle(Point(100, 360), Point(300, 430))
    three.draw(menu)
    threeText = Text(Point(200, 395), 'Cancel')
    threeText.draw(menu)

    # Initiate GameParam object
    # To be returned to gameboard.py, detailing user settings
    param = GameParam()

    # Gets mouse input 
    while True:
        mouse = menu.getMouse()
        # two at this point is "Start"
        if (two.p1.x < mouse.x and two.p2.x > mouse.x)\
                and (two.p1.y < mouse.y and two.p2.y > mouse.y):
            if oneText.getText() == 'Enter username here' or oneText.getText() == '))':

                # Displays reminder for user to enter username
                if warned == False:
                    warn = Text(Point(200, 200), 'Enter a username')
                    warn.setTextColor('red')
                    warn.draw(menu)
                    warned = True
            else:
                param.setUser(oneText.getText())
                if (warned):
                    warn.undraw()
                oneText.undraw()
                oneText = Text(Point(200, 175), 20)
                oneText.setText('Play')
                oneText.draw(menu)
                twoText.setText('Settings')
                threeText.setText('How to Play')
                four = Rectangle(Point(100, 470), Point(300, 540))
                four.draw(menu)
                fourText = Text(Point(200, 505), 'Quit Game')
                fourText.draw(menu)
                warned = False
                while True:
                    mouse = menu.getMouse()
                    # one at this point is "Play"
                    if (one.p1.x < mouse.x and one.p2.x > mouse.x) and (one.p1.y < mouse.y and one.p2.y > mouse.y):
                        menu.close()
                        return param
                    # two at this point is "Settings"
                    if (two.p1.x < mouse.x and two.p2.x > mouse.x) and (two.p1.y < mouse.y and two.p2.y > mouse.y):
                        # if settings menu is chosen, will display difficulty options
                        oneText.setText('Easy')
                        twoText.setText('Medium')
                        threeText.setText('Hard')
                        fourText.setText('Back')
                        while True:
                            # Highlights one of three choices based on selection
                            if param.difficulty == 0:
                                one.setOutline('green')
                                two.setOutline('black')
                                three.setOutline('black')
                            elif param.difficulty == 1:
                                one.setOutline('black')
                                two.setOutline('green')
                                three.setOutline('black')
                            else:
                                one.setOutline('black')
                                two.setOutline('black')
                                three.setOutline('green')
                            mouse = menu.getMouse()
                            # Checking which difficulty is clicked or back to main menu
                            # one at this point is "Easy"
                            if (one.p1.x < mouse.x and one.p2.x > mouse.x)\
                                    and (one.p1.y < mouse.y and one.p2.y > mouse.y):
                                param.setDifficulty(0)
                            # two at this point is "Medium"
                            if (two.p1.x < mouse.x and two.p2.x > mouse.x)\
                                    and (two.p1.y < mouse.y and two.p2.y > mouse.y):
                                param.setDifficulty(1)
                            # three at this point is "Hard"
                            if (three.p1.x < mouse.x and three.p2.x > mouse.x)\
                                    and (three.p1.y < mouse.y and three.p2.y > mouse.y):
                                param.setDifficulty(2)
                            # four at this point is "Back"
                            if (four.p1.x < mouse.x and four.p2.x > mouse.x)\
                                    and (four.p1.y < mouse.y and four.p2.y > mouse.y):
                                # Reset to main menu
                                one.setOutline('black')
                                two.setOutline('black')
                                three.setOutline('black')
                                four.setOutline('black')
                                oneText.setText('Play')
                                twoText.setText('Settings')
                                threeText.setText('How to Play')
                                fourText.setText('Quit Game')
                                break
                        continue
                    # three at this point is "How to Play"
                    if (three.p1.x < mouse.x and three.p2.x > mouse.x)\
                            and (three.p1.y < mouse.y and three.p2.y > mouse.y):
                        one.undraw()
                        oneText.undraw()
                        two.undraw()
                        twoText.undraw()
                        three.undraw()
                        threeText.undraw()
                        fourText.setText('Back')
                        howto = Text(Point(200, 285), """
How to Play: Mastermind
            
There is a code of four colored pegs hidden beneath the green on the board.
Guess the colors of a code of four pegs.
Click the check button to score your guess.

The small pegs on the right indicate the correctness of your guess.
White pegs represent a correct color, but in the wrong place.
Black pegs represent a correct color and correct placement.
The pegs show up in no particular order.

You have 12 tries.
Good Luck!
""")
                        howto.draw(menu)
                        while True:
                            # four at this point is "Back"
                            mouse = menu.getMouse()
                            if (four.p1.x < mouse.x and four.p2.x > mouse.x)\
                                    and (four.p1.y < mouse.y and four.p2.y > mouse.y):
                                one.draw(menu)
                                oneText.draw(menu)
                                two.draw(menu)
                                twoText.draw(menu)
                                three.draw(menu)
                                threeText.draw(menu)
                                fourText.setText('Quit Game')
                                howto.undraw()
                                break
                        continue
                    # four at this point is "Quit"
                    if (four.p1.x < mouse.x and four.p2.x > mouse.x)\
                            and (four.p1.y < mouse.y and four.p2.y > mouse.y):
                        param.setQuitting()
                        menu.close()
                        return param



        # three at this point is "Cancel"
        if (three.p1.x < mouse.x and three.p2.x > mouse.x) and (three.p1.y < mouse.y and three.p2.y > mouse.y):
            param.setQuitting()
            menu.close()
            return param
            #one2.undraw()
            #one2.draw(menu)
            #if (warned):
                #warn.undraw()
            #two2.setText('Settings')
            #three2.setText('How to Play')
            #four.draw(menu)
            #four2.draw(menu)
            #break
        continue



