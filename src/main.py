import pygame
import sys
from Constants import *
from Board import Board
from dragger import Dragger

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
            ]
        self.dragger = Dragger()
        self.dragged_square = None
        self.turn = 'w'
        pygame.display.set_caption("Chess Game")
    
    def mainLoop(self):
        run = True
        dragger = self.dragger

        
        while run:
            
            if self.dragged_square:
                board = Board(dragged_square=self.dragged_square, config=self.config, turn=self.turn)
                board.configure(self.screen)
                board.show_pieces(self.screen)
            else:
                board = Board(config=self.config, turn=self.turn)
                board.configure(self.screen)
                board.show_pieces(self.screen)
            
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEMOTION:
                    if dragger.dragging and dragger.piece is not None:
                        dragger.update_pos(event.pos)
                        dragger.piece.x = dragger.mouseX
                        dragger.piece.y = dragger.mouseY
                        dragger.drag_piece()
                        
                        
                if event.type == pygame.MOUSEBUTTONUP:
                    if dragger.piece != None and dragger.dragging:
                        if [dragger.mouseY//SIZE,dragger.mouseX//SIZE] in dragger.valid_moves:
                            self.config[dragger.init_y//SIZE][dragger.init_x//SIZE] = ''
                            self.config[dragger.mouseY//SIZE][dragger.mouseX//SIZE] = f'{dragger.piece.color}{dragger.piece.notation}'
                            self.turn = 'b' if self.turn == 'w' else 'w'
                    dragger.dragging = False
                    dragger.piece = None
                    self.dragged_square = None
                    self.valid_moves = []


                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.dragging = True
                    dragger.save_initial(event.pos)
                    dragger.update_pos(event.pos)

                    if board.squares[dragger.mouseY//SIZE][dragger.mouseX//SIZE].occupyed():
                        if board.squares[dragger.mouseY//SIZE][dragger.mouseX//SIZE].piece.color == self.turn:
                            dragger.piece = board.squares[dragger.mouseY//SIZE][dragger.mouseX//SIZE].piece

                            self.dragged_square = board.find_square(dragger.mouseY//SIZE, dragger.mouseX//SIZE)

                            dragger.valid_moves = dragger.piece.movement(board)
                            piece = dragger.piece

                if event.type == pygame.QUIT:
                    run = False

            if dragger.piece != None:
                dragger.blit_piece(self.screen)
                board.show_valid_moves(valid_moves=dragger.valid_moves,dragged_piece=piece,surface=self.screen)

            pygame.display.update()
        

main = Main()
main.mainLoop()
