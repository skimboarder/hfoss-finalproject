from constants import *
import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class ScoreTicker():
    
    def __init__(self,x, y, screen):
        self.x = x * SCORE_X
        self.y = y * SCORE_Y

        self.screen = screen
        self.score = 0
        self.msg = 'Score: '

        
    def draw(self):
        font = pygame.font.Font("freesansbold.ttf", 20)
        textSurface = font.render(self.msg + str(self.score), True, WHITE)
        self.screen.blit(textSurface, (self.x, self.y)  )
        
    def increment(self):
        print('inc score')
        self.score = self.score + 1
        self.screen.fill(BLACK)


    def reset(self):
        print('reset score')
        self.score = 0
        self.msg = 'Score: '