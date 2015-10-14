from graphics import *

#class for each playable slot
class Pegslot(Circle):
    def __init__(self):
        self.location = 0
    def setColor(self, color):
        self.setFill(color)

#create global playboard which is an 2d list of all playable slots
playboard = [[Pegslot() for i in range(4)] for j in range(12)]

def functionality(win, e):
    # takes in win (graphic) and e (exit button)

    # functionality to close window when "Exit" button is clicked
    while True:
        mouse = win.getMouse()  # pause for click in "Exit" button
        if e.p1.x < mouse.x < e.p2.x and e.p1.y < mouse.y < e.p2.y:
            win.close()
            break


def board(win):
    # takes in win (graphic) and returns e (exit button)

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
            j = j + 1
        # smaller pegs to indicate correctness of the guess
        s1 = Circle(Point(225, 62 + 40 * i), 5)
        s1.draw(win)
        s1.setFill(color_rgb(102, 51, 0))
        s2 = Circle(Point(225, 48 + 40 * i), 5)
        s2.draw(win)
        s2.setFill(color_rgb(102, 51, 0))
        s3 = Circle(Point(239, 62 + 40 * i), 5)
        s3.draw(win)
        s3.setFill(color_rgb(102, 51, 0))
        s3 = Circle(Point(239, 48 + 40 * i), 5)
        s3.draw(win)
        s3.setFill(color_rgb(102, 51, 0))
        i = i + 1
    # peg options to the left of the holes
    o1 = Circle(Point(280, 490), 10)
    o1.draw(win)
    o1.setFill('red')
    o2 = Circle(Point(310, 490), 10)
    o2.draw(win)
    o2.setFill('green')
    o3 = Circle(Point(280, 460), 10)
    o3.draw(win)
    o3.setFill('blue')
    o4 = Circle(Point(310, 460), 10)
    o4.draw(win)
    o4.setFill('yellow')
    o5 = Circle(Point(280, 430), 10)
    o5.draw(win)
    o5.setFill('orange')
    o6 = Circle(Point(310, 430), 10)
    o6.draw(win)
    o6.setFill('white')
    o7 = Circle(Point(280, 400), 10)
    o7.draw(win)
    o7.setFill('black')
    o8 = Circle(Point(310, 400), 10)
    o8.draw(win)
    o8.setFill('brown')
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
    win = GraphWin("Mastermind", 400, 600)
    e = board(win)
    functionality(win, e)


main()
