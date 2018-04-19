import pygame
import math

rightAngle = math.pi/2
line = math.pi

class Angle():
    def __init__(self, _surface, _length, _color=(255,0,0), _xpercent=.5, _ypercent=.5, _width=6,_angle=rightAngle):
		"""creates a new angle object.
			requires the surface to draw on,
			and the length of the lines.
			x and y percent define the position
			of the angle vertex in the window.
			color, width of line, and angle are
			self explanatory
		"""
        self.surface = _surface
        self.length = _length
		self.color = _color
        self.x = _surface.get_width() * _xpercent
        self.y = _surface.get_height() * _ypercent
		self.center = (self.x, self.y)
		self.bottom = (self.x + self.length, self.y)
        self.width = _width
		self.setAngle(_angle)
        
	def setAngle(self, _angle):
		ang = -_agnle
		ax = self.x + math.cos(ang) * self.length
		ay = self.y + math.sin(ang) * self.length
		self.angle = _angle
		self.top = (ax,ay)
		
    def draw(self):
        pygame.draw.line(self.surface, self.color,self.center, self.bottom ,self.width)
        pygame.draw.line(self.surface, self.color,self.center, self.top ,self.width)
		
	def getAngle(self):
		return self.angle
	
	def isObtuse(self):
		return self.angle > rightAngle
		
	def isAcute(self):
		return self.angle < rightAngle
		
	def isRight(self):
		return self.angle == rightAngle
		
	def isStraight(self):
		return self.angle == line