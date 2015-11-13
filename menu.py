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

    # Sets up buttons
    one = Rectangle(Point(100, 140), Point(300, 210))
    one.draw(menu)
    one2 = Text(Point(200, 175), 'Play')
    one2.draw(menu)
    two = Rectangle(Point(100, 250), Point(300, 320))
    two.draw(menu)
    two2 = Text(Point(200, 285), 'Settings')
    two2.draw(menu)
    three = Rectangle(Point(100, 360), Point(300, 430))
    three.draw(menu)
    three2 = Text(Point(200, 395), 'How to Play')
    three2.draw(menu)
    four = Rectangle(Point(100, 470), Point(300, 540))
    four.draw(menu)
    four2 = Text(Point(200, 505), 'Quit Game')
    four2.draw(menu)

    # Initiate GameParam object
    # To be returned to gameboard.py, detailing user settings
    param = GameParam()

    # Gets mouse input 
    while True:
        mouse = menu.getMouse()
        if (one.p1.x < mouse.x and one.p2.x > mouse.x)\
                and (one.p1.y < mouse.y and one.p2.y > mouse.y):
            # Changes and adds objects to reflect username selection menu
            one2.undraw()
            two2.setText('Start')
            three2.setText('Cancel')
            four.undraw()
            four2.undraw()
            name = Entry(Point(200, 175), 20)
            name.setText('Enter username here')
            name.draw(menu)
            while True:
                mouse = menu.getMouse()
                if (two.p1.x < mouse.x and two.p2.x > mouse.x)\
                        and (two.p1.y < mouse.y and two.p2.y > mouse.y):
                    if name.getText() == 'Enter username here' or name.getText() == '':

                        # Displays reminder for user to enter username
                        warn = Text(Point(200, 200), 'Enter a username')
                        warn.setTextColor('red')
                        warn.draw(menu)
                        warned = 1
                    else:
                        param.setUser(name.getText())
                        menu.close()
                        return param
                if (three.p1.x < mouse.x and three.p2.x > mouse.x)\
                        and (three.p1.y < mouse.y and three.p2.y > mouse.y):
                    name.undraw()
                    one2.draw(menu)
                    if (warned):
                        warn.undraw()
                    two2.setText('Settings')
                    four2.setText('Quit Game')
                    break
            continue
        if (two.p1.x < two.x and two.p2.x > mouse.x)\
                 and (two.p1.y < mouse.y and two.p2.y > mouse.y):
            # if settings menu is chosen, will display difficulty options
            one2.setText('Easy')
            two2.setText('Medium')
            three2.setText('Hard')
            four2.setText('Back')
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
                if (one.p1.x < mouse.x and one.p2.x > mouse.x)\
                        and (one.p1.y < mouse.y and one.p2.y > mouse.y):
                    param.setDifficulty(0)
                if (two.p1.x < mouse.x and two.p2.x > mouse.x)\
                        and (two.p1.y < mouse.y and two.p2.y > mouse.y):
                    param.setDifficulty(1)
                if (three.p1.x < mouse.x and three.p2.x > mouse.x)\
                        and (three.p1.y < mouse.y and three.p2.y > mouse.y):
                    param.setDifficulty(2)
                if (four.p1.x < mouse.x and four.p2.x > mouse.x)\
                        and (four.p1.y < mouse.y and four.p2.y > mouse.y):
                    # Reset to main menu
                    one.setOutline('black')
                    two.setOutline('black')
                    three.setOutline('black')
                    four.setOutline('black')
                    one2.setText('Play')
                    two2.setText('Settings')
                    three2.setText('How to Play')
                    four2.setText('Quit Game')
                    break
            continue
        if (four.p1.x < mouse.x and four.p2.x > mouse.x)\
                and (four.p1.y < mouse.y and four.p2.y > mouse.y):
            param.setQuitting()
            menu.close()
            return param
