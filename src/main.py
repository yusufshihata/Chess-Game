import pygame
import sys
from Constants import *
from Board import Board

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
    
    def mainLoop(self):
        run = True
        
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            board = Board(self.screen)
        

main = Main()
main.mainLoop()
