import pygame

from constants import * 

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class Button():
    
    def __init__(self, msg, x, y, w, h, screen, callback):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.callback = callback

    def draw(self):     
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
    
        if (self.x+self.w > mouse[0] > self.x) and (self.y+self.h > mouse[1] > self.y):
            pygame.draw.rect(self.screen, YELLOW, (self.x,self.y,self.w,self.h))
        
            if click[0] == 1:
                self.callback(self.msg)
        else:
            pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.w, self.h))

        text = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(self.msg, text)
        textRect.center = ( (self.x+(self.w/2)), (self.y+(self.h/2)) )
        self.screen.blit(textSurf, textRect)  
