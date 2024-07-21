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
    def __init__(self, surface):
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
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'white'
        self.surface = surface
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
                if self.squares[row][col].piece != None:
                    img = self.squares[row][col].piece.texture
                    imgcenter = self.squares[row][col].piece.texture_rect
                    surface.blit(img, imgcenter)
