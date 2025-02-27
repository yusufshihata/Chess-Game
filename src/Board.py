from Constants import *
from Square import Square
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Queen import Queen
from pieces.King import King
from pieces.Pawn import Pawn
import pygame
import copy


class Board:
    def __init__(self, config, turn,dragged_square=None):
        self.config = config
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.turn = turn
        self.dragged_square = dragged_square


    
    def configure(self, surface):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = Square(row, col, surface)
                if self.config[row][col] == '':
                    self.squares[row][col] = Square(row, col, surface)
                else:
                    match self.config[row][col][1]:
                        case 'R':
                            self.squares[row][col] = Square(row, col, surface, Rook(row, col, color=self.config[row][col][0]))
                        case 'N':
                            self.squares[row][col] = Square(row, col, surface, Knight(row, col, color=self.config[row][col][0]))
                        case 'B':
                            self.squares[row][col] = Square(row, col, surface, Bishop(row, col, color=self.config[row][col][0]))
                        case 'Q':
                            self.squares[row][col] = Square(row, col, surface, Queen(row, col, color=self.config[row][col][0]))
                        case 'K':
                            self.squares[row][col] = Square(row, col, surface, King(row, col, color=self.config[row][col][0]))
                        case 'P':
                            self.squares[row][col] = Square(row, col, surface, Pawn(row, col, color=self.config[row][col][0]))
        
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
            pygame.draw.circle(surface, (100,100,100), (valid_square[1]*SIZE+SIZE//2, valid_square[0]*SIZE+SIZE//2), 20)

    def find_king_pos(self):
        king_color = 'w' if self.turn == 'w' else 'b'

        for row in range(8):
            for col in range(8):
                if self.config[row][col] != '' and self.config[row][col] == f"{king_color}K":
                    return (row, col)
        return None
    

    def in_check(self, temp_board,oppo_color):
        pass


    def in_checkmate(self):
        pass

    def in_stalemate(self):
        pass