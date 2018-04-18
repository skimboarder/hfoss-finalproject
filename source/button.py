import pygame

from constants import * 

def text_objects(text, font):
    textSurface = font.render(text, True, NEGRO)
    return textSurface, textSurface.get_rect()
    
def button(msg, x, y, w, h, pantalla, callback):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(pantalla, YELLOW, (x,y,w,h))
        
        if click[0] == 1:
            callback(msg)
    else:
        pygame.draw.rect(pantalla, BLANCO, (x, y, w, h))

    text = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, text)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    pantalla.blit(textSurf, textRect)  