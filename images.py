import pygame
import math

rightAngle = math.pi/2
line = math.pi

class Image():
		
	def setImage(self, path, file):
		
		
	def __init__(self, _surface, _path, _fileName, _xpercent=.5, _ypercent=.5, _width=6,_angle=rightAngle):
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