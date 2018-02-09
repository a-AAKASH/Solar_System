from graphics import *
import math
import time

class Planets:
	def __init__(self,xpos,ypos,rad,color,major,minor,delta):
		self.x = xpos
		self.y = ypos
		self.r = rad
		self.orbitalRadius = ypos
		self.c = color
		self.planet = None
		self.a = major
		self.b = minor
		self.angle = 0
		self.changeAngle = delta

	def render(self,window):
		self.planet = Circle(Point(self.x,self.y),self.r)
		self.planet.setFill(self.c)
		self.planet.setOutline(self.c)
		self.planet.draw(window)

	def getPlanet(self):
		return self.planet	

	def getAngle(self):
		return self.angle

	def movePlanet(self):
		self.x = self.orbitalRadius*math.sin(self.angle)
		self.y = self.orbitalRadius*math.cos(self.angle)
		self.planet.move(self.x - self.planet.getCenter().getX(), self.y - self.planet.getCenter().getY())
		self.angle += self.changeAngle


def main():
	planetArray = []
	win = GraphWin("Solar System", 1200, 900)
	win.setCoords(-400,-300,400,300)
	win.setBackground("black")

	sun = Circle(Point(0,0), 20)
	sun.setFill("yellow")
	sun.setOutline("yellow")
	sun.draw(win)

	mercury = Planets(0,30,1,"grey",40,30,0.05)
	mercury.render(win)
	planetArray.append(mercury)

	venus = Planets(0,50,3,"brown",66,50,-0.04)
	venus.render(win)
	planetArray.append(venus)

	earth = Planets(0,70,5,"blue",93,70,0.03)
	earth.render(win)
	planetArray.append(earth)	

	mars = Planets(0,85,4,"red",113,85,0.035)
	mars.render(win)
	planetArray.append(mars)

	jupiter = Planets(0,150,15,"orange",200,150,0.008)
	jupiter.render(win)
	planetArray.append(jupiter)

	saturn = Planets(0,200,12,"maroon",266,200,0.01)
	saturn.render(win)
	planetArray.append(saturn)
	#moval = Oval(Point(246,200), Point(266,200))
	#moval.setOutline("White")
	#moval.draw(win)

	uranus = Planets(0,240,7,"cyan",320,240,-0.015)
	uranus.render(win)
	planetArray.append(uranus)

	neptune = Planets(0,270,7,"green",360,270,0.018)
	neptune.render(win)
	planetArray.append(neptune)

	while True:
		time.sleep(0.010)
		for eachPlanet in planetArray:
			eachPlanet.movePlanet()
	
	win.getMouse() # pause for click in window
	win.close()



if __name__ == "__main__":
	main()