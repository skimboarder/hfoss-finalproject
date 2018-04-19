#! /usr/bin/env python

import pygame

from pygame.locals import *
from angles import Angle
from button import *
from constants import *

import gtk, sys

class TuxExplorer():
    def __init__(self):
        pass
    
    def game_loop(self):

        # This is what a clicked button will call. so handle an answer here
        def saveAnswer(answer):
            # fill with black to wipe the screen. Otherwise the answer labels stack on each other
            # We wont need this when we are not outputting the answer. 
            screen.fill(BLACK);
            text = font.render(answer, True, WHITE, BLACK)
            screen.blit(text, ((x / 2) - (x / 10), (y / 2) - (y / 10)))
         
        pygame.init()
        
        global x, y, font, text, screen

        x = gtk.gdk.screen_width()
        y = gtk.gdk.screen_height() - 55

        pygame.display.set_caption('Angles')

        font = pygame.font.SysFont(None, 48)

        clock = pygame.time.Clock()
        screen = pygame.display.get_surface()
        
        angle = Angle(screen, 150, _ypercent=.3)

        while 1:
            while gtk.events_pending():
                gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Change "Juego Finalizado" to change the exit message (log)
                    exit("Game Finalized")
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)

            button("Acute", B1_X, B1_Y, BUT_W, BUT_H, screen, saveAnswer)
            button("Obtuse", B2_X, B2_Y, BUT_W, BUT_H, screen, saveAnswer)
            button("Right", B3_X, B3_Y, BUT_W, BUT_H, screen, saveAnswer)
            button("Straight Line", B4_X, B4_Y, BUT_W, BUT_H, screen, saveAnswer)
  
            angle.draw()
            
            pygame.display.flip()

            # Try to stay at 30 FPS
            clock.tick(30)
        
if __name__ == "__main__":
    TuxExplorer()
