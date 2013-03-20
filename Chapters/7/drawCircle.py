from math import pi
import turtle
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

def drawCircle(myTurtle, startingPoint, radius):
	move = 2.0 * pi * radius / 120.0
	myTurtle.up()
	myTurtle.setpos(startingPoint[0], startingPoint[1])
	myTurtle.down()
	for count in xrange(120):
		myTurtle.left(3)
		myTurtle.forward(move)
	myTurtle.mainloop()

def main():
	clearScreen()
	while True:
		try:
			xAxis = input('X axis starting point: ')
			yAxis = input('Y axis starting point: ')
			radius = input('Enter the radius: ')
			startingPoint = [xAxis, yAxis]
			break
		except NameError:
			print '\nInput must be numerical.'
			raw_input('Press ENTER to try again.')
	print "\nWe'll now draw the circle."
	print 'To exit the program when the circle is complete'
	print 'just close the window.'
	raw_input('Press ENTER to continue.')
	myTurtle = turtle
	drawCircle(myTurtle, startingPoint, radius)

main()