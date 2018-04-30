#! /usr/bin/env python

import pygame

from pygame.locals import *
from angles import Angle
from button import *
from constants import *
from images import Image
from score import ScoreTicker
import os

import gtk, sys

class TuxExplorer():
    def __init__(self):
        pass
    
    def game_loop(self):
    
        global x, y, font, text, screen
        
        # This is what a clicked button will call. so handle an answer here
        def saveAnswer(answer):
            # fill with black to wipe the screen. Otherwise the answer labels stack on each other
            # We wont need this when we are not outputting the answer. 
            if(angle.checkAnswer(answer)):
                print('correct')
                score.increment()
                angle.setRandomAngle()
                planetNear = planetFar
                planetFar = Image(PLANET_PREFIX + str(randint(0, PLANET_NUMBER - 1)) + PLANET_SUFFIX, screen)
                putPlanets(planetNear, planetFar)

            else:
                print('wrong')
                loseGame('')
                score.reset()


			
        def startGame(msg):
			global state
			state = GAME
			screen.fill(BLACK)
            
        def loseGame(msg):
            global state
            state = OVER
		
        def mainMenu(msg):
            global state
            state = MAIN
        
        def putPlanets(near, far):
            near.move(half_x, y)
            near.rect.center = near.rect.topleft
            near.scale(3)
            far.move(angle.top[0], angle.top[1])
            far.rect.center = far.rect.topleft
        
        
        pygame.init()
        


        x = gtk.gdk.screen_width()
        y = gtk.gdk.screen_height() - 55
		
        half_x = x / 2
        half_y = y / 2

        pygame.display.set_caption('Angles')

        font = pygame.font.SysFont(None, 48)

        clock = pygame.time.Clock()
        screen = pygame.display.get_surface()
        
        angleDisplay = screen.subsurface((x*.18, y*.1, x - (2*x*.18), y - (2*y*.1)))
        scoreDisplay = screen.subsurface((x*SCORE_X, y*SCORE_Y, x - (x*SCORE_X), y- (y*SCORE_Y)))
        
        angle = Angle(angleDisplay, 150, _ypercent=.3)
        
        tux = Image(TUX_IMAGE, screen)
        tux.move(half_x, half_y)
        tux.rect.midbottom = tux.rect.topleft
		
        planetNear = Image(PLANET_PREFIX + str(randint(0, PLANET_NUMBER - 1)) + PLANET_SUFFIX, screen)
        planetFar = Image(PLANET_PREFIX + str(randint(0, PLANET_NUMBER - 1)) + PLANET_SUFFIX, screen)
        putPlanets(planetNear, planetFar)
        
        score = ScoreTicker(x, y, scoreDisplay)
        
        rightBut = Button("Right", x*B1_X, y*B1_Y, x*BUT_W, y*BUT_H, screen, saveAnswer)
        acuteBut = Button("Acute", x*B2_X, y*B2_Y, x*BUT_W, y*BUT_H, screen, saveAnswer)
        obtBut = Button("Obtuse", x*B3_X, y*B3_Y, x*BUT_W, y*BUT_H, screen, saveAnswer)
		
		#Game State Stuff
        startBut = Button("Start", x*B4_X, y*B4_Y, x*BUT_W, y*BUT_H, screen, startGame)
        mainBut = Button("Main Menu", x*B5_X, y*B5_Y, x*BUT_W, y*BUT_H, screen, mainMenu)
        restartBut = Button("Restart", x*B6_X, y*B6_Y, x*BUT_W, y*BUT_H, screen, startGame)
		
        mainText = font.render("Tux Explorer", True, WHITE, BLACK)
        mainHalfWidth = mainText.get_width() / 2
        main_xpos = half_x - mainHalfWidth
        main_ypos = MAIN_Y * y
		
        overText = font.render("Game Over!", True, WHITE, BLACK)
        overHalfWidth = overText.get_width() / 2
        over_xpos = half_x - overHalfWidth
        over_ypos = OVER_Y * y
		
        global state
        state = MAIN
        
        while 1:
            while gtk.events_pending():
                gtk.main_iteration()
                
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Change "Juego Finalizado" to change the exit message (log)
                    exit("Game Finalized")
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = True

            if state == MAIN:
                screen.blit(mainText, (main_xpos, main_ypos))
                startBut.draw(clicked)
				
            elif state == GAME:
                obtBut.draw(clicked)
                acuteBut.draw(clicked)
                rightBut.draw(clicked)

                score.draw()
                
				
                angle.draw()
                tux.draw()
			
            else:
                screen.fill(BLACK)
                screen.blit(overText, (over_xpos, over_ypos))
                mainBut.draw(clicked)
                restartBut.draw(clicked)
			
            pygame.display.flip()

            # Try to stay at 30 FPS
            clock.tick(30)
        
if __name__ == "__main__":
    TuxExplorer()
