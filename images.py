import pygame
import math
import os

rightAngle = math.pi/2
line = math.pi

class Image():
		
	def setImage(self, image):
	    self.image = pygame.image.load(os.path.join('imgs', image)).convert()
		
	def move(self, x, y):
	    self.rect = self.rect.move((x,y))
	    
	def resize(self, scale):
	    self.image = pygame.transform.scale(self.image, (int(self.defRect.width*scale), int(self.defRect.height*scale)))
	    self.rect = self.image.get_rect()
	    
	def __init__(self, image, screen):
	    self.setImage(image)
	    self.defRect = self.image.get_rect()
	    self.rect = self.image.get_rect()
	    self.screen = screen
		
	def draw(self):
	    self.screen.blit(self.image,self.rect)