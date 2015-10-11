from graphics import *

def board():
	# background
	win = GraphWin("My Rectangle", 800, 600)
        r = Rectangle(Point(50, 25), Point(350, 550))
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
			p.setFill(color_rgb(102, 51, 0))
			j = j + 1
		s1 = Circle(Point(225, 62 + 40*i), 5)
		s1.draw(win)
		s1.setFill(color_rgb(102, 51, 0))
		s2 = Circle(Point(225, 48 + 40*i), 5)
		s2.draw(win)
		s2.setFill(color_rgb(102, 51, 0))
		s3 = Circle(Point(239, 62 + 40*i), 5)
		s3.draw(win)
		s3.setFill(color_rgb(102, 51, 0))
		s3 = Circle(Point(239, 48 + 40*i), 5)
                s3.draw(win)
                s3.setFill(color_rgb(102, 51, 0))
		i = i + 1
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
        win.getMouse() # pause for click in window
        win.close()
	

def main():
	board()

main()



