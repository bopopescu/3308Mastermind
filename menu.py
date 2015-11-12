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
    play = Rectangle(Point(100, 140), Point(300, 210))
    play.draw(menu)
    play2 = Text(Point(200, 175), 'Play')
    play2.draw(menu)
    settings = Rectangle(Point(100, 250), Point(300, 320))
    settings.draw(menu)
    settings2 = Text(Point(200, 285), 'Settings')
    settings2.draw(menu)
    how2play = Rectangle(Point(100, 360), Point(300, 430))
    how2play.draw(menu)
    how2play2 = Text(Point(200, 395), 'How to Play')
    how2play2.draw(menu)
    quit = Rectangle(Point(100, 470), Point(300, 540))
    quit.draw(menu)
    quit2 = Text(Point(200, 505), 'Quit Game')
    quit2.draw(menu)

    # Initiate GameParam object
    # To be returned to gameboard.py, detailing user settings
    param = GameParam()

    # Gets mouse input 
    while True:
        mouse = menu.getMouse()
        if (play.p1.x < mouse.x and play.p2.x > mouse.x)\
                and (play.p1.y < mouse.y and play.p2.y > mouse.y):
            # Changes and adds objects to reflect username selection menu
            play2.undraw()
            settings2.setText('Start')
            quit2.setText('Cancel')
            name = Entry(Point(200, 225), 20)
            name.setText('Enter username here')
            name.draw(menu)
            while True:
                mouse = menu.getMouse()
                if (settings.p1.x < mouse.x and settings.p2.x > mouse.x)\
                        and (settings.p1.y < mouse.y and settings.p2.y > mouse.y):
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
                if (quit.p1.x < mouse.x and quit.p2.x > mouse.x)\
                        and (quit.p1.y < mouse.y and quit.p2.y > mouse.y):
                    name.undraw()
                    play2.draw(menu)
                    if (warned):
                        warn.undraw()
                    settings2.setText('Settings')
                    quit2.setText('Quit Game')
                    break
            continue
        if (settings.p1.x < mouse.x and settings.p2.x > mouse.x)\
                 and (settings.p1.y < mouse.y and settings.p2.y > mouse.y):
            # if settings menu is chosen, will display difficulty options
            play2.setText('Easy')
            settings2.setText('Medium')
            quit2.setText('Hard')
            back = Rectangle(Point(100, 150), Point(140, 175))
            back.draw(menu)
            back2 = Text(Point(120, 162), 'Back')
            back2.draw(menu)
            while True:
                # Highlights one of three choices based on selection
                if param.difficulty == 0:
                    play.setOutline('green')
                    settings.setOutline('black')
                    quit.setOutline('black')
                elif param.difficulty == 1:
                    play.setOutline('black')
                    settings.setOutline('green')
                    quit.setOutline('black')
                else:
                    play.setOutline('black')
                    settings.setOutline('black')
                    quit.setOutline('green')
                mouse = menu.getMouse()
                # Checking which difficulty is clicked or back to main menu
                if (play.p1.x < mouse.x and play.p2.x > mouse.x)\
                        and (play.p1.y < mouse.y and play.p2.y > mouse.y):
                    param.setDifficulty(0)
                if (settings.p1.x < mouse.x and settings.p2.x > mouse.x)\
                        and (settings.p1.y < mouse.y and settings.p2.y > mouse.y):
                    param.setDifficulty(1)
                if (quit.p1.x < mouse.x and quit.p2.x > mouse.x)\
                        and (quit.p1.y < mouse.y and quit.p2.y > mouse.y):
                    param.setDifficulty(2)
                if (back.p1.x < mouse.x and back.p2.x > mouse.x)\
                        and (back.p1.y < mouse.y and back.p2.y > mouse.y):
                    # Reset to main menu
                    back.undraw()
                    back2.undraw()
                    play.setOutline('black')
                    settings.setOutline('black')
                    quit.setOutline('black')
                    play2.setText('Play')
                    settings2.setText('Settings')
                    quit2.setText('Quit Game')
                    break
            continue
        if (quit.p1.x < mouse.x and quit.p2.x > mouse.x)\
                and (quit.p1.y < mouse.y and quit.p2.y > mouse.y):
            param.setQuitting()
            menu.close()
            return param
