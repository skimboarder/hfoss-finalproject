import pygame
import math
import os

rightAngle = math.pi/2
line = math.pi

class Image():
		
	def setImage(self, image):
	    self.image = pygame.image.load(os.path.join('imgs', image)).convert()
	    self.originalImage = self.image
		
	def move(self, x, y):
	    print('moving' + str(x) + ', ' + str(y))
	    self.rect = self.rect.move((x,y))
	    
	def resize(self, scale):
	    self.image = pygame.transform.scale(self.image, (int(self.defRect.width*scale), int(self.defRect.height*scale)))
	    self.rect = self.image.get_rect()
	    self.defRect = pygame.Rect(self.rect[0], self.rect[1], self.defRect.height, self.defRect.width)
	    
	def setSize(self, width, height):
	    self.image = pygame.transform.scale(self.originalImage, (int(width), int(height)))
	    self.rect = self.image.get_rect();
	    
	def __init__(self, image, screen):
	    self.setImage(image)
	    self.defRect = self.image.get_rect()
	    self.rect = self.image.get_rect()
	    self.screen = screen
		
	def draw(self):
	    self.screen.blit(self.image,self.rect)
	   