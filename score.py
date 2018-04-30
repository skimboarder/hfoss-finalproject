from constants import *
import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def getHighScore():
    try:
        f = open('.highscore.txt', 'r')
        score = f.readline()
        print(score)
        return score
    except Exception as e:
        print('no file exists')
        return 0
        
class ScoreTicker():

    
    def __init__(self,x, y, screen):
        self.ttlx = x
        self.ttly = y
        self.x = x * SCORE_X
        self.y = y * SCORE_Y

        self.screen = screen
        self.score = 0
        self.msg = 'Score: '
        self.highMsg = 'High Score: ' 
        self.highScore = getHighScore()

        
    def draw(self):
        font = pygame.font.Font("freesansbold.ttf", 22)
        textSurface = font.render(self.msg + str(self.score), True, WHITE)
        self.screen.blit(textSurface, (self.x, self.y)  )

        textSurface = font.render(self.highMsg + str(self.highScore), True, WHITE)
        self.screen.blit(textSurface, (self.x, self.ttly * HSCORE_Y)  )
        
    def increment(self):
        print('inc score')
        self.score = self.score + 1
        self.screen.fill(BLACK)


    def reset(self):
        print('reset score')
        self.saveScore()
        self.highScore = getHighScore()
        self.score = 0
        self.msg = 'Score: '
        
    def saveScore(self):
        print('score : ' + str(self.score))
        print('high score : ' + str(self.highScore))
        if int(self.score) > int(self.highScore):
            print('saving...')
            try:
                f = open('.highscore.txt', 'w')
                f.write(str(self.score))
                print('saving score')
            except Exception as e:
                print('error' + str(e))
