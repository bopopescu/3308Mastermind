from graphics import *

def board():
	# background
	win = GraphWin("My Rectangle", 800, 600)
        r = Rectangle(Point(50, 25), Point(300, 550))
        r.draw(win)
        r.setFill(color_rgb(204, 102, 0))
	cover = Rectangle (Point(70, 525), Point(210, 550))
        cover.draw(win)
        cover.setFill(color_rgb(0, 153, 76))
	i = 0
	while i < 12:
		j = 0
		while j < 4:
			p = Circle(Point(80 + 40*j, 55 + 40*i), 10)
			p.draw(win)
			p.setFill('black')
			j = j + 1
		i = i + 1
        win.getMouse() # pause for click in window
        win.close()
	

def main():
	board()

main()



