import pygame
import math
from random import randint
from constants import BLACK

rightAngle = math.pi/2
line = math.pi
def randomAngle():
    return (float(randint(1,11))*15.0/180.0*math.pi)
class Angle():

    def setRandomAngle(self):
        self.setAngle(randomAngle())

    def setAngle(self, _angle):
		ang = -_angle
		ax = self.x + math.cos(ang) * self.length
		ay = self.y + math.sin(ang) * self.length
		self.angle = _angle
		self.top = (ax,ay)
		self.surface.fill(BLACK)
		
    def __init__(self, _surface, _length, _color=(96,96,96), _xpercent=.5, _ypercent=.5, _width=6,_angle=randomAngle()):
        self.surface = _surface
        self.length = _length
        self.color = _color
        self.x = _surface.get_width() * _xpercent
        self.y = _surface.get_height() * _ypercent
        self.center = (self.x, self.y)
        self.bottom = (self.x + self.length, self.y)
        self.width = _width
        self.setAngle(_angle)
		
    def draw(self):
        pygame.draw.line(self.surface, self.color, self.center, self.bottom, self.width)
        pygame.draw.line(self.surface, self.color, self.center, self.top, self.width)
        arcRect = (self.x + (math.cos(self.angle) * self.length / 10), self.y + (math.sin(self.angle) * self.length / 10), self.length / 10, self.length / 10)
        pygame.draw.arc(self.surface, self.color, arcRect, 0, self.angle)
		
    def getAngle(self):
        return self.angle
	
    def isObtuse(self):
		return self.angle > rightAngle
		
    def isAcute(self):
		return self.angle < rightAngle
		
    def isRight(self):
		return self.angle == rightAngle
		
    def checkAnswer(self, ans):
	    if ans is 'Obtuse' and self.isObtuse():
	        return True
	    elif ans is 'Acute' and self.isAcute():
	        return True
	    elif ans is 'Right' and self.isRight():
	        return True
	    return False