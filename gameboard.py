from graphics import *

def main():
    win = GraphWin("My Rectangle", 800, 600)
    r = Rectangle(Point(50, 50), Point(300, 550))
    r.draw(win)
    r.setFill('tan')
    win.getMouse() # pause for click in window
    win.close()

main()



