from Constants import *
from Square import Square
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Queen import Queen
from pieces.King import King
from pieces.Pawn import Pawn
import pygame


class Board:
    def __init__(self, surface, config,dragged_square=None):
        self.config = config
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'white'
        self.surface = surface
        self.dragged_square = dragged_square
        self.configure()
        self.show_pieces(surface)

    
    def configure(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = Square(row, col, self.surface)
                if self.config[row][col] == '':
                    self.squares[row][col] = Square(row, col, self.surface)
                else:
                    match self.config[row][col][1]:
                        case 'R':
                            self.squares[row][col] = Square(row, col, self.surface, Rook(row, col, color=self.config[row][col][0]))
                        case 'N':
                            self.squares[row][col] = Square(row, col, self.surface, Knight(row, col, color=self.config[row][col][0]))
                        case 'B':
                            self.squares[row][col] = Square(row, col, self.surface, Bishop(row, col, color=self.config[row][col][0]))
                        case 'Q':
                            self.squares[row][col] = Square(row, col, self.surface, Queen(row, col, color=self.config[row][col][0]))
                        case 'K':
                            self.squares[row][col] = Square(row, col, self.surface, King(row, col, color=self.config[row][col][0]))
                        case 'P':
                            self.squares[row][col] = Square(row, col, self.surface, Pawn(row, col, color=self.config[row][col][0]))
        
    def show_pieces(self, surface):
        for row in range(8):
            for col in range(8):
                if self.squares[row][col].piece is not None:
                    if self.dragged_square == None or (row != self.dragged_square.y or col != self.dragged_square.x):
                        img = self.squares[row][col].piece.texture
                        imgcenter = self.squares[row][col].piece.texture_rect
                        surface.blit(img, imgcenter)
    
    def find_square(self,x,y):
        return self.squares[y][x]

    def show_valid_moves(self, valid_moves, dragged_piece,surface):
        for i, valid_square in enumerate(valid_moves):
            square = self.find_square(valid_square[1], valid_square[0])
            if square.piece != None:
                if square.piece.color == dragged_piece.color:
                    valid_moves.pop(i)
            else:
                pygame.draw.circle(surface, (100,100,100), (valid_square[1]*SIZE+SIZE//2, valid_square[0]*SIZE+SIZE//2), 20)
