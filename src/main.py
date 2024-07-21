import pygame
import sys
from Constants import *
from Board import Board
from dragger import Dragger

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.dragger = Dragger()
        self.dragged_square = None
        pygame.display.set_caption("Chess Game")
    
    def mainLoop(self):
        run = True
        dragger = self.dragger

        
        while run:
            
            if self.dragged_square:
                board = Board(self.screen, self.dragged_square)
            else:
                board = Board(self.screen)
            
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEMOTION:
                    if dragger.dragging and dragger.piece is not None:
                        dragger.update_pos(event.pos)
                        dragger.piece.x = dragger.mouseX
                        dragger.piece.y = dragger.mouseY
                        dragger.drag_piece()

                        
                
                if event.type == pygame.MOUSEBUTTONUP:
                    dragger.dragging = False
                    dragger.piece = None
                    self.dragged_square = None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.dragging = True
                    dragger.update_pos(event.pos)

                    if board.squares[dragger.mouseY//SIZE][dragger.mouseX//SIZE].occupyed():
                        dragger.piece = board.squares[dragger.mouseY//SIZE][dragger.mouseX//SIZE].piece

                        self.dragged_square = board.find_square(dragger.mouseY//SIZE, dragger.mouseX//SIZE)

                if event.type == pygame.QUIT:
                    run = False

            if dragger.piece != None:
                dragger.blit_piece(self.screen)

            pygame.display.update()
        

main = Main()
main.mainLoop()
