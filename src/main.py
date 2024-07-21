import pygame
import sys
from Constants import *
from Board import Board

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    def mainLoop(self):
        run = True
        moving = False
        
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    moving = True
                if event.type == pygame.MOUSEBUTTONUP:
                    moving = False
                
                if event.type == pygame.MOUSEMOTION and moving:
                    pass
            board = Board(self.screen)
            pygame.display.update()
        

main = Main()
main.mainLoop()
