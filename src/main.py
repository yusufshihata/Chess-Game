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
        
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            board = Board(self.screen)
            pygame.display.update()
        

main = Main()
main.mainLoop()
